from django.db import models

# Create your models here.

class RestaurantLocation(models.Model):
	name			= models.CharField(max_length=120)
	location 		= models.CharField(max_length=120, null=True, blank=True)
	category    	= models.CharField(max_length=120, null=True, blank=True)
	timestamp   	= models.DateTimeField(auto_now_add=True) # elwa2t elly 2t3mlha feh create(2wl mara)
	updated			= models.DateTimeField(auto_now=True) #el wa2t elly 2a5r mara 2t3mlha feh save
	my_date_field 	= models.DateField(auto_now=False, auto_now_add=False)