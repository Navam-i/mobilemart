from django.contrib import admin

from mstore.models import Brand,Color,Tag,Product

# Register your models here.

admin.site.register(Brand)

admin.site.register(Color)

admin.site.register(Tag)

admin.site.register(Product)
