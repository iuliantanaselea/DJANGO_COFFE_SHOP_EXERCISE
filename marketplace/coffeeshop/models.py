from django.db import models


# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)  # trebuie sa fie emailuri unice

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.name

class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE) #cand stergi userul- se sterg si orderurile automat
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.user.name} ordered {self.product.name}."

class Home(models.Model):
    home = models.TextField(max_length=100)

    def __str__(self):
        return f"The Coffee Shop"