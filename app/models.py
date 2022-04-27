from django.db import models

# Create your models here.
class Outlet(models.Model):
    outletID =   models.CharField(max_length = 200, primary_key= True)     #int
    outletName = models.CharField(max_length = 200)   #varchar(20)
    area = models.CharField(max_length = 200)         #varchar(20)
    city = models.CharField(max_length = 200)         #varchar(20)
    state = models.CharField(max_length = 50)        #varchar(20)
    pincode = models.CharField(max_length = 20)      #int/varchar(20)

    def __str__(self): 
        return self.outletName

class Waiter(models.Model):
    waiterID = models.CharField(max_length = 200, primary_key= True)     #int
    firstName = models.CharField(max_length = 200)    #varchar(20)
    lastName = models.CharField(max_length = 200)     #varchar(20)
    #waiterRating =  int/float
    outletID = models.ForeignKey(Outlet, on_delete = models.CASCADE)     #int

    def __str__(self): 
        return self.firstName

    @property
    def currentOrder(self):
        return Bill.objects.filter(orderWaiter = self.waiterID).values('orderID')


class CustomerInfo(models.Model):
    customerID = models.AutoField(primary_key= True)                                     #int
    customerName = models.CharField(max_length = 200)                   #varchar
    customerPhone = models.CharField(max_length = 20)                   #int/varchar
    registrationDate = models.DateField(auto_now = True)                #date
    walletMoney = models.FloatField()                                   #float
    waiterID = models.ForeignKey(Waiter, on_delete = models.CASCADE)    #int
    def __str__(self): 
        return self.customerName

class Bill(models.Model):
    orderID = models.AutoField(primary_key= True)
    customerID = models.ForeignKey(CustomerInfo, on_delete = models.CASCADE)   #int
    orderWaiter = models.ForeignKey(Waiter, on_delete = models.CASCADE)  #int, get waiterID
    orderDate = models.DateField(auto_now = True)    #date

    @property
    def customerName(self):
        return self.customerID.customerName
    
    @property
    def customerPhone(self):
        return self.customerID.customerPhone

    @property
    def cost(self):
        it_quant = Creates.objects.filter(orderID = self.orderID).values('itemID' ,'itemQty')
        # print(it_quant)
        buffer = list(it_quant)
        # print(buffer)
        for i in buffer:
            id = i.get('itemID')
            print(id)
            k = ItemDetails.objects.filter(itemID = id).values('itemPrice','itemName')
            buffer_2 = list(k)
            #print(buffer_2)
            for j in buffer_2:
                i['itemPrice'] = j.get('itemPrice')
                i['itemName'] = j.get('itemName')
                i['costPerItem'] = i.get('itemPrice') * i.get('itemQty')
        
        # print(buffer)
        return buffer

    @property
    def total(self):
        l = self.cost
        sum = 0.00
        for k in l:
            sum = sum + k.get('costPerItem')
        return sum

    class Meta:
        unique_together = (("orderID" , "customerID"))


class OutletPhone(models.Model):
    outletID = models.ForeignKey(Outlet, on_delete = models.CASCADE,)     #int
    phoneNo = models.CharField(max_length = 10)
    
    class Meta: 
        unique_together = (("outletID", "phoneNo"))     #int/varchar

class WaiterOrderID(models.Model):
    waiterID = models.ForeignKey(Waiter, on_delete = models.CASCADE,)        #int
    orderID =  models.ForeignKey(Bill, on_delete = models.CASCADE, )  #int

    class Meta: 
        unique_together = (("waiterID", "orderID"))

    

class ItemDetails(models.Model):
    itemID = models.AutoField(primary_key=True)           #int
    itemName = models.CharField(max_length = 200)        # varchar(20)
    itemPrice = models.FloatField()        #int
    itemDescription = models.CharField(max_length = 200) #varchar(200)
    itemSize = models.BigIntegerField()         #int
    outletID = models.ForeignKey(Outlet, on_delete = models.CASCADE);        #add

    def __str__(self): 
        return self.itemName


class Inventory(models.Model):
    materialID = models.AutoField(primary_key= True)      #int
    materialQty = models.FloatField()    #int
    materialName = models.CharField(max_length = 200)     #varchar(20)
    threshQty = models.FloatField()      #int
    costPrice = models.FloatField()      #int/float
    orderedStatus = models.BooleanField() #boolean

    def __str__(self): 
        return self.materialName

    @property
    def checkQty(self):
        if self.materialQty <= self.threshQty and self.orderedStatus is False:
            return "Order pending"
        elif self.materialQty <= self.threshQty and self.orderedStatus is True: 
            return "Ordered"
        else:
            return "Sufficient Stock"

    @property
    def distributorNames(self):
        distributors = InventoryDistributor.objects.filter(materialID = self.materialID).values('distributorName')
        return distributors

class InventoryDistributor(models.Model):
    materialID = models.ForeignKey(Inventory, on_delete = models.CASCADE, )      #int
    distributorName = models.CharField(max_length = 200 )  #varchar(20)
    
    class Meta:
        unique_together = (("materialID", "distributorName"))

    @property
    def materialName(self):
        return self.materialID.materialName


class Creates(models.Model):
    #customerID = models.ForeignKey(CustomerInfo, on_delete = models.CASCADE, )      #int
    orderID = models.ForeignKey(Bill, models.CASCADE)         #int
    itemID =  models.ForeignKey(ItemDetails, on_delete = models.CASCADE, )       #int
    itemQty = models.BigIntegerField()         #int

    @property
    def itemName(self):
        return self.itemID.itemName

    @property
    def itemPrice(self):
        return self.itemID.itemPrice

    @property
    def costPerItem(self):
        return self.itemQty * self.itemPrice

    class Meta:
        unique_together = (( "orderID", "itemID"))

