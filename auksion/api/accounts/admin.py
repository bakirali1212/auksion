from django.contrib import admin
from .models import Usermodel
# Register your models here.
class UserModelAdmin(admin.ModelAdmin):
    readonly_fields = ('uuid', 'password')
    list_display = ['username', 'name', 'email', 'phone', 'role']
    
admin.site.register(Usermodel, UserModelAdmin)
