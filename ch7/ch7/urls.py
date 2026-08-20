"""
URL configuration for ch7 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
# from django.contrib import admin
# from django.urls import path
# from app1 import views as ap1
# from app2 import views as ap2

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', ap1.home,name='home'),
#     path('app1', ap1.app1,name='app1'),
#     path('app2', ap2.app2,name='app2'),
#     path('ap2me', ap2.app2_me,name='app2_me'),
# ]


'''
another way to do this 
'''

from django.contrib import admin
from django.urls import path
from app1.views import home,app1 
from app2.views import app2,app2_me 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home,name='home'),
    path('app1', app1,name='app1'),
    path('app2', app2,name='app2'),
    path('ap2me', app2_me,name='app2_me'),
]
