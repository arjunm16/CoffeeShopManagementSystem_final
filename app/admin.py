from django.contrib import admin
from .models import CustomerInfo, Bill, Outlet, OutletPhone, Waiter, WaiterOrderID, ItemDetails, Inventory, InventoryDistributor,Creates

# Register your models here.
admin.site.register(CustomerInfo)
admin.site.register(Bill)
admin.site.register(Outlet)
admin.site.register(OutletPhone)
admin.site.register(Waiter)
admin.site.register(WaiterOrderID)
admin.site.register(ItemDetails)
admin.site.register(InventoryDistributor)
admin.site.register(Inventory)
admin.site.register(Creates)