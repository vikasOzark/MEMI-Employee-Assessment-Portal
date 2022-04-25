"""MEMI_employee_assessment_cust_user URL Configuration

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
from django.urls import path, include
from accounts.views import LoginView, RegisterView, candidateintro,candidateinfo,user_login

urlpatterns = [
    path('candidateintro', candidateintro, name='candidateintro'),
    path('admin/', admin.site.urls),
    path('candidateinfo/', candidateinfo, name='candidateinfo'),
    path('login/', LoginView.as_view(), name='login'),
    path('register', RegisterView.as_view(), name='register'),
    path('user-login/<int:id>/', user_login, name='userlogin'),
    path('', include(('Assesment.urls','Assesment'), namespace='Assesment' )),



    
]
