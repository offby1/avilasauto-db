from django.db import models

# Create your models here.
#CUSTOMER MODELS
class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=11)
    email = models.EmailField()
    address = models.TextField()

    def __str__(self) -> str:
        return (f"{self.first_name} {self.last_name}")
    
class Vehicle(models.Model):
    owner = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="car_owner")
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.IntegerField()
    color = models.CharField(max_length=50)
    vin = models.CharField(max_length=17)
    license_plate = models.CharField(max_length=15)
    date_in = models.DateTimeField(auto_now_add=True)
    date_out = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=[("In Service", "In Service"), ("Ready", "Ready")], default="In Service")

    def __str__(self) -> str:
        return (f"{self.owner} {self.make} {self.model} {self.license_plate}")
    
class ServiceRecord(models.Model):
    customer_attended = models.ForeignKey(Customer, on_delete=models.PROTECT, related_name="customer_service_record")
    car_fixed = models.ForeignKey(Vehicle, on_delete=models.PROTECT, related_name="car_service_record")
    service_date = models.DateTimeField(auto_now_add=True)
    service_type = models.CharField(max_length=200)
    parts_used = models.ForeignKey("Inventory", on_delete=models.PROTECT)
    mechanic = models.ForeignKey("Mechanics", on_delete=models.PROTECT)
    service_cost = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=20, choices=[("Cash", "Cash"), ("Card", "Card")])
    payment_status = models.CharField(max_length=20, choices=[("Paid", "Paid"), ("Not Paid", "Not Paid")])
    payment_date = models.DateTimeField(null=True, blank=True)

    def __str__(self) -> str:
        return (f"{self.customer_attended} {self.car_fixed} - {self.payment_status}")
    
    def save(self, *args, **kwargs):
        if not self.pk:
            self.parts_used.stock_level -= 1
            self.parts_used.save()
        super(ServiceRecord, self).save(*args, **kwargs)

#EMPLOYEE MODELS
class Mechanics(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=11)
    email = models.EmailField()
    address = models.TextField()
    job_title = models.CharField(max_length=20)
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return (f"{self.first_name} {self.last_name} - {self.job_title}")
    
class WorkSchedule(models.Model):
    employee = models.ForeignKey(Mechanics, on_delete=models.CASCADE)
    date = models.DateField()
    time_in = models.TimeField()
    time_out = models.TimeField()

    def __str__(self) -> str:
        (f"{self.employee} - {self.date}")

#SHOP EXPENSES
class Supplier(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=11)
    email = models.EmailField()
    address = models.TextField()

    def __str__(self) -> str:
        return (f"{self.name}")

class Inventory(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.PROTECT)
    item_name = models.CharField(max_length=100)
    item_type = models.CharField(max_length=100)
    price = models.IntegerField()
    stock_level = models.IntegerField()

    def __str__(self) -> str:
        return (f"{self.item_name} {self.item_type}")
    
    def add_stock(self, new_supplies):
        self.stock_level += new_supplies
        self.save()
    
