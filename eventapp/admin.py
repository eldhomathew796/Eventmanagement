from django.contrib import admin
from eventapp.models import customer,category,event,Order,myfunction

# Register your models here.
admin.site.register(customer)
admin.site.register(category)
admin.site.register(event)
admin.site.register(Order)
admin.site.register(myfunction)
