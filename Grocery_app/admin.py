from django.contrib import admin
from . models import * #from a file called models, import all.

# Register your models here.
admin.site.register(Stockx)
admin.site.register(Sale)
admin.site.register(Branch)
admin.site.register(CreditSale)
admin.site.register(Product)


from .models import Produce

@admin.register(Produce)
class ProduceAdmin(admin.ModelAdmin):
   list_display = ('stock_type', 'total_quantity', 'image')
