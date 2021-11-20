from django import forms
from .models import Product
from .models import Customer
from django.forms import MultiWidget


class SearchForm(forms.Form):
    first_name = forms.CharField(widget= forms.TextInput(attrs={"placeholder": "Enter name here"}))

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

class ProductForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "your title"}))
    description = forms.CharField(required=False, widget=forms.Textarea(
        attrs={
             "class": "new class name two",
             "id": "my id for textarea",
             "placeholder": "Enter Description here",
             "rows": 20,
            "cols": 120
         }))
    summary = forms.CharField(required=False, widget=forms.Textarea(
        attrs={
             "class": "new class name two",
             "id": "my id for textarea",
             "placeholder": "Enter Summary here",
             "rows": 20,
            "cols": 120
         }))
    price = forms.DecimalField(decimal_places=2, max_digits=10000)

    class Meta:
        model = Product
        fields = [  # set what fields our form will have
            'title',
            'price',
            'summary',
            'description',
            'stock',
        ]

class RawForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "your title"}))
    description = forms.CharField(required=False, widget=forms.Textarea(
        attrs={
            "class": "new class name two",
            "id": "my id for textarea",
            "placeholder": "Enter Description here",
            "rows": 20,
            "cols": 120
        }))
    price = forms.DecimalField(decimal_places=2, max_digits=10000)
