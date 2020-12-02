"""wallet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls import url
from backend import views 

handler404 = 'backend.views.home_err'
handler500 = 'backend.views.home_err500'
handler403 = 'backend.views.home_err'
handler400 = 'backend.views.home_err'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('wallet/<wallet_name>/', views.wallet_page, name="wallet_page"),
    path('add-wallet/', views.add_wallet, name="add_wallet"),
    path('delete-wallet/', views.delete_wallet, name="delete_wallet"),
    path('add-transaction/', views.add_transaction, name="add_transaction"),
    path('delete-transaction/', views.delete_transaction, name="delete_transaction"),
    path('', views.home, name="home_page"),
    url(r'^(.*)$', views.home), # every other url
]
