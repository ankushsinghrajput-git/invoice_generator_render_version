from django.db import models


class Invoice(models.Model):
    customer_name = models.CharField(max_length=255)
    customer_number = models.CharField(max_length=15)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Invoice {self.id} - {self.customer_name}"
