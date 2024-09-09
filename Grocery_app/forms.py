from django.forms import ModelForm
from .models import *
from django.core.exceptions import ValidationError
from django import forms
from .models import CreditSale

class SaleForm(ModelForm):
    class Meta:
        model = Sale
        fields = ['quantity', 'amount_received', 'issued_to', 'modality']



class CreditSaleForm(forms.ModelForm):
    class Meta:
        model = CreditSale
        fields = ['product', 'client_name', 'quantity', 'id_nin_number', 'contact', 'address', 'branch']


class ProduceForm(forms.ModelForm):
    class Meta:
        model = Produce
        fields = ['stock_type', 'total_quantity', 'image']


class AddForm(forms.ModelForm):
    class Meta:
        model = Stockx
        fields = ['total_quantity'] #Its the only field that needs to be updated when stock is added by the sales agent.

      
        