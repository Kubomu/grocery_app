from django.urls import path
#We are accessing the views file which is found in our application folder.(Grocery_app)
from Grocery_app import views
#accessing the views of admin_app,the second app
#from admin_app import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('login2/',auth_views.LoginView.as_view(template_name = 'Grocery_app/login2.html'), name = 'login2'),
    path('home/',views.home,name = "home"),
    path('home/<int:product_id>/', views.product_detail,name = 'product_detail'),
    path('',views.index,name ="index"),
    path('home/<int:product_id>/', views.delete_detail,name = 'delete_detail'),
    path('delete/<int:product_id>/',views.delete_detail,name = 'delete_detail'),
    path('logout/', auth_views.LoginView.as_view(template_name = 'Grocery_app/logout.html'), name = 'logout'),
    path('receipt/',views.receipt,name = 'receipt'),
    path('receipt/<int:receipt_id>',views.receipt_detail,name='receipt_detail'),
    path('credit_sale/', views.credit_sale, name='credit_sale'),
    path('credit_sale_list/', views.credit_sale_list, name='credit_sale_list'),
    path('approve_credit_sale/<int:sale_id>/', views.approve_credit_sale, name='approve_credit_sale'),
    path('products/<int:product_id>/', views.product_detail, name='product_detail'),
    #path('products/', views.Product, name='products'),
    path('add/', views.add_produce, name='add_produce'),
    path('', views.produce_list, name='produce_list'),
    path('add_to_stock/<str:pk>/', views.add_to_stock, name='add_to_stock'),
    path('issue_item/<str:pk>/', views.issue_item, name='issue_item'),
    path('all_sales/', views.all_sales, name='all_sales'),
   
]

# Add this line to serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

