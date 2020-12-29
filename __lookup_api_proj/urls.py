"""__lookup_api_proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from .CustomAuthToken import CustomAuthToken
from companies.api.viewsets import CompaniesViewSet
from users.api.viewsets import UsersViewSet
from customers.api.viewsets import CustomerViewSet
from buy.api.viewsets import BuyViewSet
from c_cards.api.viewsets import CardViewSet
from products.api.viewsets import ProductViewSet
from categories.api.viewsets import CategoryViewSet
from sales.api.viewsets import SaleViewSet
from cash.api.viewsets import CashViewSet
from expenses.api.viewsets import ExpenseViewSet
from rest_framework import routers
from django.conf.urls import include

router = routers.DefaultRouter()
router.register(r'companies', CompaniesViewSet)
router.register(r'buy', BuyViewSet, basename="Buy")
router.register(r'c_cards', CardViewSet, basename="Card")
router.register(r'cash', CashViewSet, basename="Cash")
router.register(r'categories', CategoryViewSet, basename="Category")
router.register(r'customers', CustomerViewSet, basename="Customer")
router.register(r'expenses', ExpenseViewSet, basename="Expense")
router.register(r'products', ProductViewSet, basename="Product")
router.register(r'sales', SaleViewSet, basename="Sale")
router.register(r'users', UsersViewSet, basename="User")

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-token-auth/', CustomAuthToken.as_view())
]
