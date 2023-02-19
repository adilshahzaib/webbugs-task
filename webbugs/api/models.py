from django.db import models


class Supplier(models.Model):
    name = models.CharField(max_length=50)

    address = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Shop(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name='shops')

    def __str__(self):
        return self.name
