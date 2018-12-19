from . import views
from django.conf.urls import url , include

app_name = 'xuqiu_info'
urlpatterns = [
    url(r'^add_xuqiu_info/' , views.add_xuqiu_info , name='add_xuqiu_info') ,
    url(r'^xuqiu_info_page/' , views.xuqiu_info_page , name='xuqiu_info_page') ,
]