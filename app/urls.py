from django.urls import path
from .views import CustomerList, CustomerDetail, BillList,BillDetails,WaiterList, WaiterDetail,InventoryList, InventoryDetail

urlpatterns = [
    path('customers/<int:pk>/', CustomerDetail.as_view()),
    path('customers/', CustomerList.as_view()),
    path('bills/', BillList.as_view()),
    path('bills/<int:pk>/', BillDetails.as_view()),
    path('waiter/', WaiterList.as_view()),
    path('waiter/<int:pk>/', WaiterDetail.as_view()),
    path('inventory/', InventoryList.as_view() ),
    path('inventory/<int:pk>', InventoryDetail.as_view()),

    #path('addbill/<int:pk>', )
    
]