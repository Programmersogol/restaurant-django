from django.db import models
from slugify import slugify
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.conf import settings



class Customer(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=11)
    password = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    date_modified=models.DateTimeField(User,auto_now=True)
    phone=models.CharField(max_length=25,blank=True)
    address=models.CharField(max_length=250,blank=True)
    city=models.CharField(max_length=250,blank=True)
    state=models.CharField(max_length=250,blank=True)
    zipcode=models.CharField(max_length=250,blank=True)
    country=models.CharField(max_length=250,default='IRAN')


    def __str__(self):
        return self.user.username
    
def creat_profile(sender,instance,created,**kwargs):
    if created:
        usee_profile=Profile(user=instance)  
        usee_profile.save()

post_save.connect(creat_profile,sender=User)        

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="نام دسته‌بندی")
    slug = models.SlugField(unique=True, verbose_name="اسلاگ", blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name.lower())
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "دسته‌بندی"
        verbose_name_plural = "دسته‌بندی‌ها"

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="دسته‌بندی")
    name = models.CharField(max_length=200, verbose_name="نام محصول")
    slug = models.SlugField(unique=True, verbose_name="اسلاگ", blank=True)
    image = models.ImageField(upload_to='files/cover', verbose_name="تصویر")
    price = models.DecimalField(max_digits=10, decimal_places=0, verbose_name="قیمت")
    description = models.TextField(verbose_name="توضیحات", blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name.lower())
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "محصول"
        verbose_name_plural = "محصولات"

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name="کاربر")
    session_id = models.CharField(max_length=100, null=True, blank=True, verbose_name="شناسه سشن")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")

    def __str__(self):
        return f"سبد خرید {'کاربر ' + str(self.user) if self.user else 'ناشناس ' + self.session_id}"

    class Meta:
        verbose_name = "سبد خرید"
        verbose_name_plural = "سبدهای خرید"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, verbose_name="سبد خرید")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="محصول")
    quantity = models.PositiveIntegerField(default=1, verbose_name="تعداد")

    def __str__(self):
        return f"{self.quantity} عدد {self.product.name}"

    class Meta:
        verbose_name = "آیتم سبد خرید"
        verbose_name_plural = "آیتم‌های سبد خرید"

class ContactMessage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    message = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.user.username if self.user else 'Anonymous'}"
   
   
    class Meta:
        verbose_name = "نظر"
        verbose_name_plural= "نظرات"
