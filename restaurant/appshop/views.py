from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .forms import SingUpForm, UpdateUserForm, UpdatePasswordForm, UpdateUserInfo, ContactForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponseRedirect, JsonResponse
from .models import Category, Product, CartItem, Cart, Profile
from django.views.decorators.http import require_POST
import json
from django.contrib.auth.decorators import login_required


# صفحه اصلی سایت (نیازمند لاگین)
@login_required(login_url='logins')
def home(request):
    products = Product.objects.all()  # گرفتن همه محصولات
    return render(request, 'index.html', {'products': products})


# نمایش صفحه دسته‌بندی‌ها
def category(request):
    return render(request, 'catagory.html')


# صفحه تماس با ما (فرم ارسال پیام)
def contact(request):
    return render(request, 'contact.html')


# ثبت‌نام کاربر جدید
def SingUp(request):
    if request.method == "POST":
        form = SingUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password1 = form.cleaned_data["password1"]
            password2 = form.cleaned_data["password2"]

            # بررسی برابری رمز عبور و تکرار آن
            if password1 != password2:
                messages.error(request, "رمز عبور و تکرار آن یکسان نیستند.")
                return redirect("SingUp")

            # بررسی وجود نام کاربری
            if User.objects.filter(username=username).exists():
                messages.error(request, "این نام کاربری قبلاً ثبت شده است.")
                return redirect("SingUp")

            # ایجاد کاربر جدید
            user = User.objects.create_user(username=username, password=password1)
            user.save()
            messages.success(request, f"{username} عزیز با موفقیت ثبت‌نام شدید.")
            return redirect("update_info")
        else:
            messages.error(request, "لطفاً فرم را به‌درستی پر کنید.")
    else:
        form = SingUpForm()

    return render(request, "singup.html", {"form": form})


# ورود کاربر
def logins(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f"{username} عزیز با موفقیت وارد شدید.")
            return HttpResponseRedirect('update_info')
        else:
            messages.error(request, "اطلاعات را به درستی وارد کنید...خطا")
            redirect("logins")
    return render(request, 'login.html')


# خروج کاربر
def logouts(request):
    logout(request)
    messages.success(request, "با موفقیت خارج شدید")
    return HttpResponseRedirect('/')


# ویرایش اطلاعات کاربر
def update_user(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        userform = UpdateUserForm(request.POST or None, instance=current_user)

        if request.method == "POST":
            if userform.is_valid():
                userform.save()
                login(request, current_user)  # بروزرسانی session بعد از ویرایش
                messages.success(request, "پروفایل شما با موفقیت ویرایش شد")
                return redirect('/')
        
        return render(request, 'update_user.html', {"form": userform})
    
    else:
        messages.error(request, "کاربر عزیز ابتدا باید وارد حساب کاربری خود شوید")
        return redirect('logins')


# ویرایش رمز عبور
def update_password(request):
    if request.user.is_authenticated:
        curent_user = request.user
        if request.method == 'POST':
            form = UpdatePasswordForm(curent_user, request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'رمز با موفقیت ویرایش شد')
                login(request, curent_user)
                return redirect('update_user')
            else:
                for error in list(form.errors.values()):
                    messages.error(request, error)
                return redirect('update_password')
        else:
            form = UpdatePasswordForm(curent_user)
            return render(request, 'update_password.html', {'form': form})

    else:
        messages.success(request, 'کاربر عزیز ابتدا لاگین کنید')
        return redirect('logins')


# ویرایش اطلاعات پروفایل
def update_info(request):
    if request.user.is_authenticated:
        current_user = Profile.objects.get(user__id=request.user.id)
        form = UpdateUserInfo(request.POST or None, instance=current_user)

        if form.is_valid():
            form.save()
            messages.success(request, 'اطلاعات کاربری شما ویرایش شد')
            return redirect('/')
        return render(request, 'update_info.html', {'form': form})
    else:
        messages.success(request, 'کاربر عزیز ابتدا لاگین کنید')
        return redirect('logins')


# جزئیات دسته‌بندی و محصولات مربوطه
def category_detail(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    return render(request, 'category_detail.html', {'category': category, 'products': products})


# افزودن محصول به سبد خرید
@require_POST
def add_to_cart(request):
    try:
        data = json.loads(request.body)
        product_slug = data.get('product_slug')
        quantity = int(data.get('quantity', 1))
        product = get_object_or_404(Product, slug=product_slug)

        if request.user.is_authenticated:
            cart, created = Cart.objects.get_or_create(user=request.user)
        else:
            session_id = request.session.session_key
            if not session_id:
                request.session.create()
                session_id = request.session.session_key
            cart, created = Cart.objects.get_or_create(session_id=session_id)

        cart_item, created = CartItem.objects.get_or_create(
            cart=cart,
            product=product,
            defaults={'quantity': quantity}
        )
        if not created:
            cart_item.quantity += quantity
            cart_item.save()

        return JsonResponse({'success': True, 'message': 'محصول به سبد خرید اضافه شد!'})
    except Exception as e:
        return JsonResponse({'success': False, 'message': str(e)})


# تعداد محصولات در سبد خرید
def cart_item_count(request):
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user).first()
    else:
        session_id = request.session.session_key
        cart = Cart.objects.filter(session_id=session_id).first()

    if cart:
        count = sum(item.quantity for item in cart.cartitem_set.all())
    else:
        count = 0

    return JsonResponse({'cart_item_count': count})


# نمایش جزئیات سبد خرید
def cart_detail(request):
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user).first()
    else:
        session_id = request.session.session_key
        cart = Cart.objects.filter(session_id=session_id).first()

    total_price = 0
    if cart:
        for item in cart.cartitem_set.all():
            total_price += item.quantity * item.product.price

    return render(request, 'cart.html', {'cart': cart, 'total_price': total_price})


# بروزرسانی تعداد آیتم در سبد خرید
@require_POST
def update_cart_item(request):
    try:
        data = json.loads(request.body)
        item_id = data.get('item_id')
        quantity = int(data.get('quantity'))

        cart_item = get_object_or_404(CartItem, id=item_id)
        if quantity >= 1:
            cart_item.quantity = quantity
            cart_item.save()

        total_price = sum(item.quantity * item.product.price for item in cart_item.cart.cartitem_set.all())
        return JsonResponse({
            'success': True,
            'quantity': cart_item.quantity,
            'price': cart_item.product.price,
            'total_price': total_price
        })
    except Exception as e:
        return JsonResponse({'success': False, 'message': str(e)})


# حذف آیتم از سبد خرید
@require_POST
def remove_cart_item(request):
    try:
        data = json.loads(request.body)
        item_id = data.get('item_id')

        cart_item = get_object_or_404(CartItem, id=item_id)
        cart = cart_item.cart
        cart_item.delete()

        total_price = sum(item.quantity * item.product.price for item in cart.cartitem_set.all())
        return JsonResponse({'success': True, 'total_price': total_price})
    except Exception as e:
        return JsonResponse({'success': False, 'message': str(e)})


# جستجوی محصولات
def search(request):
    query = request.POST.get('top-search', '').strip()
    products = []
    if query:
        products = Product.objects.filter(name__icontains=query) | Product.objects.filter(category__name__icontains=query)
    return render(request, 'search_result.html', {'query': query, 'products': products})


# فرم تماس با کاربر (نیازمند لاگین)
@login_required
def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_message = form.save(commit=False)
            contact_message.user = request.user 
            contact_message.save()
            messages.success(request, "پیام شما با موفقیت ارسال شد ✅")
            return redirect("contact")  
    else:
        form = ContactForm()

    return render(request, "contact.html", {"form": form})


# نمایش صفحه درباره ما
def about(request):
    return render(request, "about.html")
