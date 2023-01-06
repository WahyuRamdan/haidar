from django.contrib import admin
from .models import * 

class MapsAdmin(admin.ModelAdmin):
    list_display = ['club']

class CrudAdmin(admin.ModelAdmin):
    list_display = ['nama_pemain']


admin.site.register(Maps, MapsAdmin)
admin.site.register(Crud, CrudAdmin)