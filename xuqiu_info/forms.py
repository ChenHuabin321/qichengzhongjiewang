from django import forms   #使用了表单类，必须导入django自带的forms类
from .models import Xuqiu_info

class Add_xuqiu_info_form(forms.ModelForm):#如果要更改数据库，则继承forms.ModelForm；如果只是读取数据库则继承forms.Form
    class Meta:
        model = Xuqiu_info
        fields = ('name' , 'jiating_address' , 'phone' , 'xuqiuliang' ,
                  'caizhairiqi' ,  'guojin_min' , 'guojin_max',  'qita')