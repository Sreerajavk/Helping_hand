"""helping_hand URL Configuration

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
from django.urls import path, re_path
from django.conf.urls import url

from donate import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , views.index) ,
    path('home/' , views.home ) ,
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),

    path('login/', views.login_fn) ,
    path('signup_inst/' , views.signup_inst) ,


    path('signup/' , views.signup , name = 'signup') ,
    path('mobile_login/' , views.mobile_login) ,
    path('mobile_signup/' , views.mobile_signup) ,
    path('add_post/' , views.add_post , name = 'add_post') ,

    path('view_post/' , views.view_post , name = 'view_post') ,
    path('email_status/' , views.email_status )
]
