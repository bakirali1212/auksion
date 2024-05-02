from django.contrib import admin
from .models import Productmodel, Category, Certificatemodel
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
admin.site.register(Productmodel)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Certificatemodel)
