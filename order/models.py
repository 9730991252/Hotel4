from django.db import models

# Create your models here.

class Marketing_Employee (models.Model):
    employee_name = models.CharField(max_length=100)
    employee_address=models.CharField(max_length=100)
    employee_mobile=models.IntegerField(default=True,unique=True)
    pin = models.IntegerField()
    added_date = models.DateTimeField(auto_now_add=True, null=True)
    status = models.IntegerField(default=1)





class Hotel(models.Model):
    marketing_employee = models.ForeignKey(Marketing_Employee,on_delete=models.PROTECT,default=True)
    hotel_name = models.CharField(max_length=100)
    owner_name=models.CharField(max_length=100)
    hotel_address = models.CharField(max_length=100)
    mobile=models.IntegerField(unique=True)
    pin = models.IntegerField()
    status=models.IntegerField(default=1)
    marketing_admin_status=models.IntegerField(default=1)
    added_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.hotel_name


class Employee (models.Model):
    hotel_id = models.CharField(max_length=100,null=True,blank=True)
    employee_name = models.CharField(max_length=100)
    employee_address=models.CharField(max_length=100)
    employee_mobile=models.IntegerField(unique=True)
    pin = models.IntegerField()
    department=models.CharField(max_length=50,default=True)
    added_by = models.CharField(max_length=50, default=True)
    added_date = models.DateTimeField(auto_now_add=True, null=True)
    status = models.IntegerField(default=1)



class Dish_category(models.Model):
    category_name = models.CharField(max_length=100)
    hotel_id = models.CharField(max_length=100,null=True,blank=True)
    added_date = models.DateTimeField(auto_now_add=True, null=True)
    status = models.IntegerField(default=1)


class Dish(models.Model):
    dish_name = models.CharField(max_length=100)
    dish_marathi_name = models.CharField(max_length=100,default=True)
    dish_category = models.ForeignKey(Dish_category,on_delete=models.PROTECT,default=True)
    price=models.FloatField(default=0)
    hotel_id = models.CharField(max_length=100,null=True,blank=True)
    added_date = models.DateTimeField(auto_now_add=True, null=True)
    status = models.IntegerField(default=1)


class Table(models.Model):
    table_number = models.CharField(max_length=100)
    hotel = models.ForeignKey(Hotel,on_delete=models.PROTECT,default=True)
    added_date = models.DateTimeField(auto_now_add=True, null=True)
    status = models.IntegerField(default=1)

STATUS_CHOICES = (
  ('Accepted','Accepted'),
  ('Pending','Packed'),
  ('Delivered','Delivered'),
  ('Cancel','Cancel'),
)



class Cart(models.Model):
    dish=models.ForeignKey(Dish,on_delete=models.PROTECT,default=True)
    dish_marathi_name = models.CharField(max_length=100,default=True)
    table=models.ForeignKey(Table,on_delete=models.PROTECT,default=True)
    table_number = models.CharField(max_length=100,null=True,blank=True)
    hotel = models.ForeignKey(Hotel,on_delete=models.PROTECT,default=True)
    employee = models.ForeignKey(Employee,on_delete=models.PROTECT,null=True,blank=True)
    chef_id = models.CharField(max_length=100,null=True,blank=True)
    qty = models.IntegerField(default=1)
    price=models.FloatField(default=0,null=True)
    total_price=models.FloatField(default=0,null=True)
    note=models.CharField(max_length=100,null=True)
    cook_status = models.IntegerField(default=0)
    status = models.CharField(choices=STATUS_CHOICES,default='Pending',max_length=50)
    added_date = models.DateTimeField(auto_now_add=True, null=True)






class NewCart(models.Model):
    dish=models.ForeignKey(Dish,on_delete=models.PROTECT,default=True)
    dish_marathi_name = models.CharField(max_length=100,default=True)
    table=models.ForeignKey(Table,on_delete=models.PROTECT,default=True)
    table_number = models.CharField(max_length=100,null=True,blank=True)
    hotel = models.ForeignKey(Hotel,on_delete=models.PROTECT,default=True)
    employee = models.ForeignKey(Employee,on_delete=models.PROTECT,null=True,blank=True)
    chef_id = models.CharField(max_length=100,null=True,blank=True)
    qty = models.IntegerField(default=1)
    price=models.FloatField(default=0,null=True)
    total_price=models.FloatField(default=0,null=True)
    note=models.CharField(max_length=100,null=True)
    cook_status = models.IntegerField(default=0)
    status = models.CharField(choices=STATUS_CHOICES,default='pending',max_length=50)
    added_date = models.DateTimeField(auto_now_add=True, null=True)










class OrderMaster(models.Model):
    hotel = models.ForeignKey(Hotel,on_delete=models.PROTECT,default=True)
    table=models.ForeignKey(Table,on_delete=models.PROTECT,default=True)
    total_price=models.FloatField(default=0,null=True)
    ordered_date = models.DateTimeField(auto_now_add=True,null=True)
    order_filter=models.IntegerField(default=True)


class OrderDetail(models.Model):
    hotel = models.ForeignKey(Hotel,on_delete=models.PROTECT,default=True)
    dish=models.ForeignKey(Dish,on_delete=models.PROTECT,null=True)
    table_number=models.IntegerField(default=True)
    dish_marathi_name = models.CharField(max_length=100,default=True)
    qty = models.IntegerField(default=1)
    price=models.FloatField(default=0,null=True)
    total_price=models.FloatField(default=0,null=True)
    ordered_date = models.DateTimeField(auto_now_add=True,null=True)
    date=models.DateField(auto_now_add=True,null=True)
    order_filter=models.IntegerField(default=True)



