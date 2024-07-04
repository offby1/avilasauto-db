from django.shortcuts import render, redirect
from .models import Customer, Vehicle, ServiceRecord, Mechanics, WorkSchedule, Supplier, Inventory
from .forms import CustomerForm, VehicleForm, ServiceRecordForm

# Create your views here.

def add_customer(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("customer_list")
        else:
            form = CustomerForm()
        return render(request, "add_customer.htnl", {"form": form})
    
def customer_list(request):
    customers = Customer.objects.all()
    return render(request, "customer_list.html", {"customers": customers})