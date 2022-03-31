"""mysite1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^page1', views.page1_view),
    # 通过正则配置/page3， page4
    # 匹配规则是自上而下的,如果把这条放到最上面,那么上面的两条永远都不会被匹配到了
    re_path(r'page(\d+)', views.pagen_view),
    
    # 多个分组
    re_path(r'^(\d+)/(\w{3})/(\d+)', views.math_view),
    
    # 使用捕获组
    re_path(r'person/(?P<name>\w+)/(?P<age>\d{1,2})', views.person_view),
    
    # 分组练习,同一个视图处理函数,利用正则的分组传参显示接受不同的参数
    re_path(r'birthday/(?P<y>\d{4})/(?P<m>\d{1,2})/(?P<d>\d{1,2})', views.birthday_view),
    re_path(r'birthday/(?P<m>\d{1,2})/(?P<d>\d{1,2})/(?P<y>\d{4})/', views.birthday_view),
]
