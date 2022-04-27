from dataclasses import field
from rest_framework import serializers
from .models import CustomerInfo, Bill, Outlet, OutletPhone, Waiter, WaiterOrderID, ItemDetails, Inventory, InventoryDistributor,Creates

class CustomerInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerInfo
        fields = ('customerID', 'customerName', 'customerPhone', 'registrationDate', 'walletMoney', 'waiterID')

class BillInfoSerializer(serializers.ModelSerializer):
    customerName = Bill.customerName
    cost = Bill.cost
    total = Bill.total
    phone = Bill.customerPhone
    class Meta:
        model = Bill
        fields = ('orderID','customerName', 'customerPhone', 'cost', 'total')

class WaiterinfoSerializer(serializers.ModelSerializer):
    currentOrder = Waiter.currentOrder
    class Meta:
        model = Waiter
        fields = ('waiterID', 'firstName', 'lastName','currentOrder','outletID')

class InventoryInfoSerializer(serializers.ModelSerializer):
    checkQty = Inventory.checkQty
    class Meta:
        model = Inventory
        fields = ('materialID', 'materialName', 'materialQty', 'costPrice', 'checkQty', 'threshQty', 'distributorNames' )

