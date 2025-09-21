from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Order, OrderItem, ShippingAddress
from appshop.models import Cart, CartItem


def checkout(request):
    """
    نمایش صفحه تسویه‌حساب
    - اگر کاربر وارد شده باشد، سبد خرید بر اساس کاربر گرفته می‌شود.
    - اگر کاربر مهمان باشد، سبد خرید بر اساس session_id گرفته می‌شود.
    - محاسبه آیتم‌های سبد و مجموع قیمت کل
    """
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user).first()
    else:
        session_id = request.session.session_key
        if not session_id:
            request.session.create()
            session_id = request.session.session_key
        cart = Cart.objects.filter(session_id=session_id).first()

    cart_items = []
    total_price = 0
    if cart:
        cart_items = CartItem.objects.filter(cart=cart)
        total_price = sum(item.quantity * item.product.price for item in cart_items)

    context = {
        'cart_items': cart_items,
        'total_price': total_price,
    }
    return render(request, 'payment/checkout.html', context)


@login_required
def create_order_from_cart(request):
    """
    ایجاد سفارش از سبد خرید:
    - فقط با متد POST امکان‌پذیر است.
    - اگر سبد خرید خالی باشد، پیام خطا نمایش داده می‌شود.
    - بررسی تکمیل بودن نام و نام خانوادگی کاربر.
    - انتخاب آدرس ارسال از پروفایل یا ShippingAddress.
    - ایجاد رکورد Order و OrderItem.
    - حذف آیتم‌های سبد پس از ایجاد سفارش.
    """
    if request.method == 'POST':
        cart = Cart.objects.filter(user=request.user).first()
        if not cart or not cart.cartitem_set.exists():
            messages.error(request, "سبد خرید خالی است.")
            return redirect('category')

        cart_items = cart.cartitem_set.all()
        total = sum(item.quantity * item.product.price for item in cart_items)

        # بررسی نام و نام خانوادگی
        if not request.user.first_name or not request.user.last_name:
            messages.warning(request, "لطفاً ابتدا پروفایل خود را تکمیل کنید.")
            return redirect('update_user')

        full_name = f"{request.user.first_name} {request.user.last_name}".strip() or request.user.username
        email = request.user.email or "email@default.com"

        # انتخاب آدرس ارسال
        profile = request.user.profile if hasattr(request.user, 'profile') else None
        shipping_address_obj = ShippingAddress.objects.filter(user=request.user).first()

        if profile and profile.address:
            shipping_address_text = f"{profile.address}, {profile.city}, {profile.state}, {profile.zipcode}, {profile.country}"
        elif shipping_address_obj:
            shipping_address_text = f"{shipping_address_obj.shipping_address1}, {shipping_address_obj.shipping_city}, {shipping_address_obj.shipping_state}, {shipping_address_obj.shipping_zipcode}, {shipping_address_obj.shipping_country}"
        else:
            shipping_address_text = "آدرس ثبت نشده، لطفاً آدرس خود را وارد کنید."

        # ایجاد سفارش
        order = Order.objects.create(
            user=request.user,
            full_name=full_name,
            email=email,
            shipping_address=shipping_address_text,
            amount_paid=total,
        )

        # ایجاد آیتم‌های سفارش
        for item in cart_items:
            OrderItem.objects.create(
                order=order,
                products=item.product,
                user=request.user,
                quantity=item.quantity,
                price=item.product.price,
            )

        # پاک کردن آیتم‌های سبد
        cart_items.delete()

        return redirect('order_detail', order_id=order.id)

    return redirect('checkout')


@login_required
def order_detail(request, order_id):
    """
    نمایش جزئیات یک سفارش:
    - گرفتن سفارش مربوط به کاربر وارد شده
    - محاسبه مجموع کل قیمت سفارش
    """
    order = get_object_or_404(Order, id=order_id, user=request.user)
    order_items = OrderItem.objects.filter(order=order)
    total_price = sum(item.quantity * item.price for item in order_items)

    context = {
        'order': order,
        'order_items': order_items,
        'total_price': total_price,
    }
    return render(request, 'payment/order_detail.html', context)


@login_required
def fake_payment(request, order_id):
    """
    شبیه‌سازی پرداخت:
    - اگر وضعیت سفارش 'pending' باشد، به 'paid' تغییر می‌کند.
    - پیام موفقیت یا هشدار در صورت پرداخت قبلی یا لغو.
    """
    order = get_object_or_404(Order, id=order_id, user=request.user)

    if order.status == 'pending':
        order.status = 'paid'
        order.save()
        messages.success(request, "✅ پرداخت با موفقیت شبیه‌سازی شد")
    else:
        messages.warning(request, "⚠️ این سفارش قبلاً پرداخت شده یا لغو شده است")

    return redirect("order_detail", order_id=order.id)
