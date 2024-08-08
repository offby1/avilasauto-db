from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("add_customer/", views.add_customer, name="add_customer"),
    path("customers/", views.customer_list, name="customer_list")
]