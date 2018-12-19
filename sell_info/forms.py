from django import forms   #使用了表单类，必须导入django自带的forms类
from .models import Guoyuan_info
from django.forms import widgets
from django.forms import fields

class Add_sell_info_form(forms.ModelForm):#如果要更改数据库，则继承forms.ModelForm；如果只是读取数据库则继承forms.Form
    class Meta:
        model = Guoyuan_info
        fields = ('name' , 'jiating_address' , 'phone' , 'shuliang' ,
                  'chanliang' , 'guoyuan_address' , 'guojin_max' , 'guojin_max' ,'qita')

