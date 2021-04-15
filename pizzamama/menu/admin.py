from django.contrib import admin
from .models import Pizza


class PizzaAdmin(admin.ModelAdmin):
    list_display = ('nom', 'ingredients', 'vegetarienne', 'prix')
    search_fields = ['nom', 'ingredients']

# Register your models here.
admin.site.register(Pizza, PizzaAdmin)