from django.db import models

class Sales(models.Model):
    customer_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Sale by {self.customer_name} at {self.location}"

class SalesProduct(models.Model):
    sales = models.ForeignKey(Sales, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantity}x {self.product_name} in sale {self.sales}"
