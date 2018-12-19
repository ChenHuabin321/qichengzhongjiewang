"""qicheng URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import home_page , about_us
from django.conf.urls import url , include




urlpatterns = [
    path('admin/', admin.site.urls),
    #url(r'home/',TemplateView.as_view(template_name="home.html"), name="home"),
    #url(r'^$',TemplateView.as_view(template_name="home.html"), name="home"),
    url(r'^$', home_page , name="home"),
    url(r'^about_us/', about_us , name="about_us"),
    # url(r'^pifa/$', pifa_page , name="pifa"),
    # url(r'^caigou/$', caigou_page , name="caigou"),
    url(r'^xuqiu/' , include('xuqiu_info.urls' , namespace = 'xuqiu_info') ) ,
    url(r'^sell/' , include('sell_info.urls' , namespace = 'sell_info')),
]
