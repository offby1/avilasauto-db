from django.urls import path
from . import views

urlpatterns = [
    path("add_customer/", views.add_customer, name="add_customer"),
    path("customesr/", views.customer_list, name="customer_list")
]