from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import csv
from bistro_app.models import Ingredient


class IngredientsForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = '__all__'

    ingredients = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Ingredients'
        }
    ))

    quantity_stock = forms.FloatField(required=True, widget=forms.NumberInput(
        attrs={
            'min': '0',
            'class': 'form-control',
            'placeholder': 'Quantity_stock'
        }
    ))

    unit = forms.CharField(widget=forms.NumberInput(
        attrs={
            'min': '0',
            'class': 'form-control',
            'placeholder': 'Units'
        }
    ))

    price_unit = forms.FloatField(widget=forms.NumberInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Price/Unit'
        }
    ))

    min_stock = forms.FloatField(required=True, widget=forms.NumberInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Minimum Stock'
        }
    ))

    alert_stock = forms.FloatField(required=True, widget=forms.NumberInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Stock almost empty'
        }
    ))

    remarks = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'placeholder': 'Comments'
        }
    ))

    lot = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Lot'
        }
    ))

    entry_date = forms.DateTimeField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'YYYY-MM-DD'
        }
    ))


class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),
            # 'password1': forms.PasswordInput(attrs={'placeholder': 'Password'}),
            # 'password2': forms.PasswordInput(attrs={'placeholder': 'Re-entry your password'}),
        }

