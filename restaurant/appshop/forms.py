from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm,SetPasswordForm
from .models import Profile,ContactMessage




class SingUpForm(forms.Form):
    Name= forms.CharField(required=True, label="نام کامل")
    username = forms.CharField(required=True, label="نام کابری")
    Phone = forms.CharField(required=True, label="شماره تلفن")
    password1 = forms.CharField(required=True, label="پسوورد", widget=forms.PasswordInput)
    password2 = forms.CharField(required=True, label="تکرار پسوورد", widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super(SingUpForm, self).__init__(*args, **kwargs)
        for i in SingUpForm.visible_fields(self):
            i.field.widget.attrs["class"] = "form-control"


class UpdateUserForm(UserChangeForm):
    password=None
    first_name=forms.CharField(label='',required=True,max_length=50,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'نام خود را وارد کنید'}))
    last_name = forms.CharField(label='',required=True, max_length=50, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'نام خانوادگی خود را وارد کنید'}))

    email = forms.EmailField(label='',required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'ایمیل خود را وارد کنید'}))

    username = forms.CharField(label='',required=True, max_length=20, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'نام کاربری خود را وارد کنید'}))



    class Meta:

        model=User
        fields=('first_name','last_name','email','username')


class UpdatePasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(label='',required=True,widget=forms.PasswordInput(attrs={'class':'form-control','name':'password','type':'password','placeholder':'رمز بالای 8 کاراکتر وارد کنید:'}))

    new_password2 = forms.CharField(label='',required=True, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'name': 'password', 'type': 'password',
               'placeholder': 'دوباره رمز خود را وارد کنید:'}))

    class Meta:
        model=User
        fields=['new_password1','new_password2']


class UpdateUserInfo(forms.ModelForm):
    phone=forms.CharField(label='',required=True,max_length=11,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'شماره تلفن خود را وارد کنید'}))
    address=forms.CharField(label='',required=True,max_length=250,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'آدرس خود را وارد کنید'}))
    city=forms.CharField(label='',required=True,max_length=50,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'شهر خود را وارد کنید'}))
    country=forms.CharField(label='',required=True,max_length=50,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'کشور خود را وارد کنید'}))

    class Meta:
        model=Profile
        fields=('phone','address','city','country')





class ContactForm(forms.ModelForm):
    message = forms.CharField(
        label='',
        required=True,
        max_length=500,
        widget=forms.Textarea(attrs={'class': 'form-control w-full p-3 border rounded-lg', 'placeholder': 'شنوای نظرت هستیم', 'rows': 4})
    )

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control w-full p-3 border rounded-lg focus:ring-2 focus:ring-brand-500'})

    class Meta:
        model = ContactMessage
        fields = ['message']