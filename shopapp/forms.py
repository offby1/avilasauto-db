from django import forms
from .models import Customer, Vehicle, ServiceRecord

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = '__all__'

class ServiceRecordForm(forms.ModelForm):
    class Meta:
        model = ServiceRecord
        fields = '__all__'