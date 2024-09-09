from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
import uuid

# Create your models here.
class Stockx(models.Model):
    item_name = models.CharField(max_length=50, null=True, blank=True)
    stock_type = models.CharField(max_length=50, null=True, blank=True)
    stock_source = models.CharField(max_length=50, null=True, blank=True)
    unit_cost = models.IntegerField(default=0, null=True, blank=True)
    unit_price = models.IntegerField(default=0, null=True, blank=True)
    total_quantity = models.IntegerField(default=0, null=True, blank=True)
    stock_branch = models.CharField(max_length=50, null=True, blank=True)
    stock_date = models.DateTimeField(auto_now_add=True, null=True, blank=True) #Automtically sets it when object is first recorded.
    stock_time = models.TimeField(auto_now_add=True, null=True, blank=True)
    stock_dealer = models.CharField(max_length=50, null=True, blank=True)
    stock_contact = models.IntegerField(default=0, null=True, blank=True)
    issued_quantity = models.IntegerField(default=0, null=True, blank=True)
    
    
    

    def __str__(self):
        return self.item_name
#We have created one class that suites a given table






class Sale(models.Model):
    CASH = 'cash'
    CREDIT = 'credit'
    
    SALE_MODALITY_CHOICES = [
        (CASH, 'Cash'),
        (CREDIT, 'Credit'),
    ]
    #associating property item with the name of the stock being kept in the stock table/model.
    item = models.ForeignKey(Stockx,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    amount_received = models.IntegerField(default=0, null=True, blank=True)
    issued_to = models.CharField(max_length=50, null=True, blank=True)
    unit_price = models.IntegerField(default=0, null=True, blank=True)
    date_sold = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    receipt_number = models.PositiveIntegerField(unique=True, blank=True, null=True)
    modality = models.CharField(
        max_length=6, 
        choices=SALE_MODALITY_CHOICES,  
        default=CASH,  
    )


    """def save(self, *args, **kwargs):
        if not self.receipt_number:
            last_sale = Sale.objects.all().order_by('id').last()
            self.receipt_number = (last_sale.receipt_number + 1) if last_sale else 1
        super(Sale, self).save(*args, **kwargs)"""

    
    
      
      
    def get_total(self):
    # Set default values to 0 if quantity or unit_price is None
        quantity = self.quantity if self.quantity is not None else 0
        unit_price = self.unit_price if self.unit_price is not None else 0
        total = quantity * unit_price
        return int(total)

    def get_change(self):
    # Ensure amount_received is not None, defaulting to 0 if it is
        amount_received = self.amount_received if self.amount_received is not None else 0
    
    # Get the total price
        total_price = self.get_total()
    
    # Calculate change
        change = amount_received - total_price
    
    # Return the absolute value of the change
        return abs(int(change))

    def __str__(self):
        return self.item.item_name
 


class Branch(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    
    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class CreditSale(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    client_name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    id_nin_number = models.CharField(max_length=20)
    contact = models.CharField(max_length=20)
    address = models.TextField()
    sales_agent = models.ForeignKey(User, on_delete=models.CASCADE, related_name='credit_sales')
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    approved_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='approved_credit_sales')
    
    def __str__(self):
        return f"Credit Sale for {self.client_name} - {self.product.name}"
    

class Produce(models.Model):
    # Update your model fields as needed
    stock_type = models.CharField(max_length=255)
    total_quantity = models.PositiveIntegerField()  # Example field for quantity
    image = models.FileField()  # Field for image upload
    
    def __str__(self):
        return self.stock_type  # Use stock_type as the display name



    