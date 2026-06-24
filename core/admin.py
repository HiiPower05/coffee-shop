from django.contrib import admin
from core.models import Category, MenuItem

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Category, CategoryAdmin)



class MenuItemAdmin(admin.ModelAdmin):
    pass

admin.site.register(MenuItem, MenuItemAdmin)