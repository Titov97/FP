from django import forms
from django.core.exceptions import ValidationError

from bistro_app.models import Ingredients


class IngredientsForm(forms.ModelForm):
    class Meta:
        model = Ingredients
        fields = '__all__'

    ingredients = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Ingredients'
        }
    ))

    quantity_stock = forms.FloatField(required=True, min_value=0, widget=forms.NumberInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Quantity_stock'
        }
    ))

    unit = forms.CharField(min_value=0, widget=forms.NumberInput(
        attrs={
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


