from django.db import models
class RegistationData(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    mobile=models.BigIntegerField()
    email=models.EmailField(max_length=100)
    gender=models.CharField(max_length=10)
    date_of_birth=models.DateField(max_length=100)

class ProductData(models.Model):
    product_id=models.IntegerField()
    product_name=models.CharField(max_length=100)
    product_cost=models.IntegerField()
    product_class=models.CharField(max_length=20)
    no_of_products=models.IntegerField()
    manufacture_date=models.DateField(max_length=100)
    expiry_date=models.DateField(max_length=100)
    customer_name=models.CharField(max_length=100)
    mobile=models.BigIntegerField()
    email=models.EmailField(max_length=100)

