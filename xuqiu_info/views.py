from django.shortcuts import render
from .forms import Add_xuqiu_info_form
from django.http import HttpResponse

def xuqiu_info_page(request):
    return render(request, "xuqiu_info/xuqiu_info_page.html")

def add_xuqiu_info(request):
    if request.method == "POST" :
        add_sell_info_form = Add_xuqiu_info_form(request.POST)
        print('999999')
        if add_sell_info_form.is_valid():
            print('11111111111111:表单验证有效')
            new_sell_info = add_sell_info_form.save(commit=False)
            new_sell_info.save()
            return HttpResponse('您填写的信息已提交，我们将在3个工作日内联系您，审核通过后我们将在官网上发布您的信息。')
        else:
            return HttpResponse('对不起，您的信息提交失败，请重试。')
    else:#如果尚未提交信息，只是第一次打开链接，则打开空表单
        add_xuqiu_info_form = Add_xuqiu_info_form()
        return render(request , 'xuqiu_info/add_xuqiu_info.html' , {'form':add_xuqiu_info_form})

