from django.contrib import admin

# Register your models here.
from .models import Guoyuan_info

class Sell_info_admin(admin.ModelAdmin):
    list_display = ('name' , 'shuliang' , 'chanliang' , 'jiating_address' , 'guojin_min' , 'guojin_max', 'guoyuan_address' , 'phone' , 'publish' , 'is_checked')
    list_filter = ('chanliang' , 'jiating_address' , 'is_checked')

admin.site.register(Guoyuan_info , Sell_info_admin)