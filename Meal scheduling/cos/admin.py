from django.contrib import admin
from .models import Order
# Register your models here.
from .models import menu_card
admin.site.register(menu_card)
admin.site.register(Order)

