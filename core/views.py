from django.shortcuts import render
from .models import Category
# Create your views here.
def home(request):
    categories = Category.objects.order_by('display_order')

    template_name = "core/index.html"
    return render(request, template_name, {'categories': categories})