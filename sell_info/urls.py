from . import views
from django.conf.urls import url , include

app_name = 'sell_info'
urlpatterns = [
    url(r'^sell_info/' , views.sell_info_page , name='sell_info_page'),
    url(r'^add_sell/' , views.add_sell_info , name='add_sell_info') ,
]