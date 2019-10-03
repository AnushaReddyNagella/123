"""PersonalWebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from mysite import views
from django.views.generic import TemplateView
from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns



urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name='mysite/base.html'), name='base'),
    url(r'^Home$', views.Home, name='Home'),
    url(r'DataSceience$', views.DataSceience, name='DataSceience'),
    url(r'^AboutUs$',views.AboutUs,name='AboutUs'),
    url(r'^AmazonWebServices$',views.AmazonWebServices,name='AmazonWebServices'),
    url(r'^BigDataAnalytics$',views.BigDataAnalytics,name='BigDataAnalytics'),
    url(r'^ContactUs$',views.ContactUs,name='ContactUs'),
    url(r'^Corporate$',views.Corporate,name='Corporate'),
    url(r'^DigitalMarketing$',views.DigitalMarketing,name='DigitalMarketing'),
    url(r'^Blog$',views.Blog,name='Blog'),
    url(r'^ClassRoomLED$',views.ClassRoomLED, name='ClassRoomLED'),
    url(r'^LiveOnline$', views.LiveOnline, name=' LiveOnline'),
    url(r'^OurServies$', views.OurServies, name='OurServies'),
    url(r'^Reviews$', views.Reviews, name='Reviews'),
    url(r'^ SummerCamp$', views.SummerCamp, name=' SummerCamp'),
    url(r'^ChatbotForBusinessApplication$', views.Workshop, name=' Workshop'),

]
urlpatterns+=staticfiles_urlpatterns()
