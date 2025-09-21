from django import forms
from .models import ShippingAddress

class ShippingForm(forms.ModelForm):
    shipping_full_name = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}),
        required=True,
    )

    shipping_email = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
        required=True,
    )

    shipping_phone = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone'}),
        required=True,
    )

    shipping_address1 = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Addres1'}),
        required=True,
    )

    shipping_city = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'City'}), 
        required=True
    )

    shipping_state = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'State'}), 
        required=False
    )
    
    
    shipping_zipcode = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'ZipCode'}), 
        required=False
    )


    shipping_country = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Country'}), 
        required=True
    )

    shipping_old_cart = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'OldCart'}), 
        required=True
    )


    class Meta:
        model = ShippingAddress
        fields=('shipping_full_name',
                'shipping_email',
                'shipping_phone',
                'shipping_address1',
                'shipping_city',
                'shipping_state',
                'shipping_zipcode',
                'shipping_country',
                'shipping_old_cart')
        
        exclude=['user',]




    