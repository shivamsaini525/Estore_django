from django.db import models

class Customer(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.EmailField()
    phone=models.CharField(max_length=20)
    image=models.ImageField(upload_to='uploads/customer/')
    address=models.CharField(max_length=60)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=80)
    password=models.CharField(max_length=500)
    

    def register(self):
        self.save()

