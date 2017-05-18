from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
# Create your models here.

class Restaurant(models.Model):
	name=models.CharField(max_length=250)
	location=models.CharField(max_length=500)
	email=models.EmailField()
	mobile=models.CharField(max_length=10)
	def __str__(self):
		return self.name
	def get_absolute_url(self):
		return  reverse('app:restaurant-index')

class Item(models.Model):
	item=models.CharField(max_length=100)
	price=models.IntegerField()
	restaurant=models.ForeignKey(Restaurant,on_delete=models.CASCADE)
	image=models.FileField()
	def __str__(self):
		return self.item+' '+self.restaurant.name
	def get_absolute_url(self):
		return  reverse('app:item-index')
class Address(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	name=models.CharField(max_length=250)
	mobile=models.IntegerField()
	email=models.EmailField()
	address=models.CharField(max_length=1000)
	def __str__(self):
		return self.item+' '+self.restaurant.name