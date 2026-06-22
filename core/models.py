from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    # The order you want the category to display on the page
    display_order = models.IntegerField(default=0) 

    def __str__(self):
        return self.name
    

class MenuItem(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='items')
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True, help_text="Brief description of ingredients")
    price = models.DecimalField(max_digits=6, decimal_places=2) 
    is_available = models.BooleanField(default=True) 

    def __str__(self):
        return self.name
    
class Location(models.Model):
    branch_name = models.CharField(max_length=100) 
    address = models.CharField(max_length=255)
    operating_hours = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.branch_name