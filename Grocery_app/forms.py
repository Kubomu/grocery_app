from django.forms import ModelForm
from .models import *
from django.core.exceptions import ValidationError
from django import forms
from .models import CreditSale
from django.core.validators import MinValueValidator

class SaleForm(ModelForm):
    class Meta:
        model = Sale
        fields = ['quantity', 'amount_received', 'issued_to']
        
        labels = {
            'quantity': 'Quantity',
            'amount_received': 'Amount Received',
            'issued_to': 'Issued To', 
            #'modality': 'Modality',
            
        }

        quantity = forms.CharField(max_length=50, validators=[MinValueValidator(1)], error_messages={'required': 'Please fill in the quantity', 'max_length': 'Quantity should  not be longer than 50 characters'}, widget=forms.TextInput(attrs={'placeholder':'1', 'type': 'number'}), required=False)
    
        amount_received = forms.CharField(max_length=50, error_messages={'required':'Please enter amount paid', 'max_length':'Amount should not be more than 50 characters'}, widget=forms.TextInput(attrs={'placeholder': '50000', 'type': 'number'}), required=False)
    
        issued_to = forms.CharField(max_length=20, error_messages={'required':'Please enter a name', 'max_length':'Name should not be more than 20 characters'}, widget=forms.TextInput(attrs={'placeholder': 'Melissa Bloom'}), required=False)
    
        #modality = forms.CharField(error_messages={'required':'Please select mode of payment'}, widget=forms.DateInput(attrs={'placeholder': 'select'}), required=False)
    



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

 

        