from django.contrib import admin
from .models import Customer,Category,Product,Profile,ContactMessage
from django.contrib.auth.models import User
# Register your models here.

admin.site.register(Customer)
admin.site.register(Profile)
admin.site.register(ContactMessage)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'formatted_price')
    admin.site.register(Category)
    admin.site.register(Product)


class ProfileInLine(admin.StackedInline):
    model = Profile
 

class UserAdmin(admin.ModelAdmin):
    model=User    
    fields=['username','first_name','last_name','email']
    inlines=[ProfileInLine]


admin.site.unregister(User)
admin.site.register(User,UserAdmin)    
