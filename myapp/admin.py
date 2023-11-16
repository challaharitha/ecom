from django.contrib import admin
from myapp.models import Product,Cart,Buy
admin.site.register(Product)
admin.site.register(Cart)
# Register your models here.
admin.site.register(Buy)

