from django.contrib import admin

# Register your models here.
from .models import Xuqiu_info

class Xiuqiu_info_admin(admin.ModelAdmin):
    list_display = ('name' , 'xuqiuliang' , 'guojin_min' , 'guojin_max' ,'jiating_address' ,
                    'caizhairiqi' , 'phone' , 'publish' , 'is_checked')
    list_filter = ('xuqiuliang' , 'caizhairiqi' , 'is_checked')







admin.site.register(Xuqiu_info , Xiuqiu_info_admin)