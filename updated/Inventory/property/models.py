from django.db import models

# Create your models here.
class Office(models.Model):
    off_name = models.CharField(max_length=100)

    def __str__(self):
         return self.off_name


class Person(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    office_name= models.ForeignKey(Office, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Equipment(models.Model):
    qty = models.CharField(max_length=5)
    unit = models.CharField(max_length=5)
    desc1 =models.TextField()
    desc2 = models.TextField()
    date_acquired = models.DateField()
    prop_num = models.CharField(max_length=10)
    unit_cost = models.DecimalField(max_digits=10, decimal_places=2)
    total_cost =models.DecimalField(max_digits=10, decimal_places=2)
    location = models.TextField(max_length=100)
    user = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
        return self.qty
