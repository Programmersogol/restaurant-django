# restaurant-django
<<<<<<< HEAD
Django restaurant website | رستوران آنلاین با جنگو
=======
Restaurant Project with Django
>>>>>>> d6633675e5a240f9e0bf68a5bd5954d5f9f8d28d



🍽️ رستوران رضوی - Restaurant Razavi
یک سیستم کامل رستوران آنلاین با Django که شامل منوی دیجیتال، سبد خرید هوشمند، سیستم پرداخت، و مدیریت سفارشات می‌شه. این پروژه با عشق و دقت برای تجربه‌ای بی‌نظیر از سفارش آنلاین غذا طراحی شده! ✨
📋 ویژگی‌ها
🚀 امکانات اصلی

منوی کامل رستوران: نمایش دسته‌بندی‌های مختلف (پیتزا، برگر، نوشیدنی) با تصاویر باکیفیت
جستجوی هوشمند: جستجو در محصولات و دسته‌بندی‌ها با فیلتر دقیق
سبد خرید پیشرفته: 
افزودن/حذف محصولات
کنترل تعداد با دکمه‌های +/-
آپدیت real-time جمع کل
آیکون سبد با شمارنده


صفحه صورت‌حساب شیک: نمایش خلاصه سفارش با طراحی مدرن
مدیریت سفارشات: ثبت و نمایش جزئیات کامل سفارشات
نقشه و تماس: نمایش موقعیت رستوران روی Google Maps

🎨 طراحی و تجربه کاربری

طراحی ریسپانسیو: کاملاً سازگار با موبایل، تبلت، و دسکتاپ
تم رستورانی جذاب: رنگ‌های گرم (زرد-نارنجی) و فونت فارسی Vazir
انیمیشن‌های نرم: ورود تدریجی المان‌ها با Animate.css
حالت تاریک: قابلیت تغییر تم با toggle
فونت فارسی: استفاده از Vazirmatn برای خوانایی بهتر

🛡️ امنیت و عملکرد

احراز هویت: سیستم لاگین/رجیستر کامل
CSRF Protection: محافظت کامل در برابر حملات CSRF
مدیریت Session: پشتیبانی از کاربران مهمان و لاگین‌شده
بهینه‌سازی: لود سریع و کد تمیز

🏗️ تکنولوژی‌های استفاده‌شده



Frontend
Backend
Database
Tools



HTML5
Django 5.2.4
SQLite
Git/GitHub


CSS3
Python 3.11.4
-
VS Code


Bootstrap
-
-
Tailwind CSS


jQuery
-
-
-


Animate.css
-
-
-


📁 ساختار پروژه
restaurant-project/
├── restaurant/
│   ├── appshop/
│   │   ├── models.py          # مدل‌های محصولات و سبد خرید
│   │   ├── views.py           # ویوهای اصلی
│   │   ├── templates/         # قالب‌های اصلی
│   │   └── templatetags/      # فیلترهای سفارشی
│   ├── payment/
│   │   ├── models.py          # مدل‌های سفارش و آدرس
│   │   ├── views.py           # ویوهای پرداخت
│   │   └── templates/         # قالب‌های پرداخت
│   ├── settings.py            # تنظیمات پروژه
│   ├── urls.py               # URLهای اصلی
│   └── manage.py
├── static/
│   ├── css/
│   ├── img/
│   └── js/
└── templates/
    └── base.html             # قالب اصلی

🚀 راه‌اندازی سریع
پیش‌نیازها

Python 3.8+
pip

نصب و اجرا
# کلون کردن پروژه
git clone https://github.com/yourusername/restaurant-razavi.git
cd restaurant-razavi

# ایجاد محیط مجازی
python -m venv venv
source venv/bin/activate  # Linux/Mac
# یا venv\Scripts\activate  # Windows

# نصب وابستگی‌ها
pip install -r requirements.txt

# مهاجرت دیتابیس
python manage.py makemigrations
python manage.py migrate

# ایجاد سوپریوزر
python manage.py createsuperuser

# اجرای سرور
python manage.py runserver

دسترسی

صفحه اصلی: http://127.0.0.1:8000/
ادمین: http://127.0.0.1:8000/admin/
سبد خرید: http://127.0.0.1:8000/cart/

🛠️ نحوه استفاده
1. مدیریت محصولات

برو به /admin/ و لاگین شو
توی بخش Appshop → Products محصولات رو اضافه کن
دسته‌بندی‌ها رو هم از Categories مدیریت کن

2. سبد خرید

محصولات رو به سبد اضافه کن
تعداد رو با دکمه‌های +/- تنظیم کن
جمع کل به‌صورت real-time آپدیت می‌شه

3. پرداخت

روی "ادامه به پرداخت" کلیک کن
جزئیات سفارش رو بررسی کن
سفارش رو تأیید کن

4. مدیریت سفارشات

توی /admin/ بخش Payment → Orders رو چک کن
وضعیت سفارشات رو تغییر بده (در انتظار، پرداخت‌شده، لغو‌شده)

📱 اسکرین‌شات‌ها

🎨 تم و استایل
رنگ‌ها

اصلی: #b0c364 (سبز زیتونی)
ثانویه: #f4a261 (نارنجی گرم)
پس‌زمینه: #fafafa (خاکستری روشن)
متن: #2d3748 (خاکستری تیره)

فونت

Vazirmatn: فونت فارسی مدرن و خوانا

🔧 تنظیمات پیشرفته
اضافه کردن درگاه پرداخت
برای ادغام درگاه‌های ایرانی مثل زرین‌پال:
# settings.py
ZARINPAL_MERCHANT_ID = 'your-merchant-id'

ارسال پیامک
برای اطلاع‌رسانی سفارشات با قاصدک:
# settings.py
GHASEDAK_API_KEY = 'your-api-key'

تنظیمات ایمیل
# settings.py
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@gmail.com'
EMAIL_HOST_PASSWORD = 'your-password'

📝 نکات مهم
امنیت

از {% csrf_token %} توی همه فرم‌ها استفاده کن
رمز عبور رو با make_password هش کن
API Keyها رو توی متغیرهای محیطی ذخیره کن

بهینه‌سازی

تصاویر رو فشرده کن (حداکثر 100KB)
از CDN برای فایل‌های استاتیک استفاده کن
کش مرورگر رو فعال کن

🤝 مشارکت
اگر دوست داری مشارکت کنی:

یه fork از ریپو بگیر
تغییراتت رو توی branch جدید بساز
Pull Request بفرست

📄 لایسنس
این پروژه تحت MIT License منتشر شده.
📞 پشتیبانی
برای سؤالات، با ایمیل sogolvafa23@gmail.com  تماس بگیر یا توی Issues مشکلت رو مطرح کن.

ساخته شده با 💕 برای رستوران رضوی
