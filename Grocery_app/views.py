from django.shortcuts import render, redirect, get_object_or_404
#accessing our models so we can get content from them
from Grocery_app.models import *   #it means from Grocery _app, in the models.py file, import all
#borrowing decorators from django to restrict access to our pages
from django.contrib.auth.decorators import login_required
#importing a response to delete
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from .forms import SaleForm, AddForm
from django.contrib.auth.views import LogoutView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login, logout
from .filters import StockFilter
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import CreditSale, Product, Branch, Produce
from .forms import CreditSaleForm, ProduceForm
from django.contrib.auth import authenticate, login as auth_login


# Create your views here.
def index(request):
    items = Stockx.objects.all().order_by('-id')
    return render(request,'Grocery_app/index2.html', {'items': items})


@login_required
def home(request):
    products = Stockx.objects.all().order_by('-id') #we're creating a variable called stock, arranged by their orders called ids
    #applying filters to a query set
    product_filters = StockFilter(request.GET, queryset=products)
    products = product_filters.qs
    return render(request, 'Grocery_app/home.html', {'products': products, 'product_filters': product_filters})

@login_required
def product_detail(request,product_id):
    product = Stockx.objects.filter(id = product_id)
    return render(request,'Grocery_app/product_detail.html',{'product':product})

@login_required
def delete_detail(request,product_id):
    product = Stockx.objects.get(id = product_id)
    product.delete()
    return HttpResponseRedirect(reverse('home'))

@login_required
def issue_item(request,pk):
    #accessing all items in the stock model
    issued_item = Stockx.objects.get(id = pk)
    #accessing our form 
    sales_form = SaleForm(request.POST)
    #receiving data from the form and saving from the model


    if request.method == 'POST':
        #checking whether the form is valid
        if sales_form.is_valid():
            new_sale = sales_form.save(commit = False)
            new_sale.item = issued_item
            new_sale.unit_price = issued_item.unit_price
            new_sale.save()
            #keep track of sales remaining after sales
            issued_quantity = int(request.POST['quantity'])
            issued_item.total_quantity -= issued_quantity
            issued_item.save()

            return redirect('receipt')

    return render(request, 'Grocery_app/issue_item.html',{'sales_form':sales_form})

def all_sales(request):
    sales = Sale.objects.all().order_by('-id')
    total_expected = sum([items.get_total() or 0  for items in sales])
    total = sum([items.amount_received or 0 for items in sales])
    total_change = sum([items.get_change() or 0  for items in sales])
    net = total_expected - total
    return render(request, 'Grocery_app/all_sales.html', {'sales': sales, 'total': total, 'total_change': total_change, 'net': net, 'total_expected': total_expected})

@login_required
def receipt(request):
    sales = Sale.objects.all().order_by('-id')
    return render(request, 'Grocery_app/receipt.html', {'sales': sales})

@login_required
def receipt_detail(request, receipt_id):
    receipt = Sale.objects.get(id = receipt_id)
    return render(request, 'Grocery_app/receipt_detail.html', {'receipt': receipt})


#class LogoutView(LogoutView):
def loginout(request):
        #logout(request)
        return render(request, 'Grocery_app/logout.html')
    

def LoginView(LoginView):
     pass
    


@login_required
def credit_sale(request):
    if request.method == 'POST':
        form = CreditSaleForm(request.POST)
        if form.is_valid():
            credit_sale = form.save(commit=False)
            credit_sale.sales_agent = request.user
            credit_sale.save()
            return redirect('credit_sale_list')
    else:
        form = CreditSaleForm()
    
    return render(request, 'Grocery_app/credit_sale.html', {'form': form})

@login_required
def credit_sale_list(request):
    credit_sales = CreditSale.objects.all()
    return render(request, 'Grocery_app/credit_sale_list.html', {'credit_sales': credit_sales})

@user_passes_test(lambda u: u.is_staff)
def approve_credit_sale(request, sale_id):
    credit_sale = get_object_or_404(CreditSale, id=sale_id)
    credit_sale.approved = True
    credit_sale.approved_by = request.user
    credit_sale.save()
    return redirect('credit_sale_list')



def add_produce(request):
    if request.method == 'POST':
        form = ProduceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('produce_list')  # Replace with your desired URL name
    else:
        form = ProduceForm()
    return render(request, 'add_produce.html', {'form': form})

def produce_list(request):
    items = Produce.objects.all()
    return render(request, 'produce_list.html', {'items': items})



@login_required
def add_to_stock(request, pk):
    # creating the variable which will access all the objects
    issued_item = Stockx.objects.get(id=pk)
    # creating a form to be used to post out data to be saved to the database
    form = AddForm(request.POST)
    if request.method == 'POST':
        # confirming that if some submits to send the submiiting request, 
        # if the form is valid , proceed 
        if form.is_valid():
            # filtering the field posted from the form is converted to interger and gv to da added quantity variable
            added_quantity = int(request.POST['total_quantity'])
            # here were adding the quantity coming from the form and add it wz da value currently in the database"issued_total_quantity"
            issued_item.total_quantity += added_quantity
            # saving the results got after addding the added quantity
            issued_item.save()
            # used for debugging , to print the actual values in the terminal"nt so crucial".
            print(added_quantity)
            print(issued_item.total_quantity)
            # going baclk to our home to continue.
            return redirect('home')
    #   help us render our data  # 
    return render(request, 'Grocery_app/add_to_stock.html', {'form':form})




