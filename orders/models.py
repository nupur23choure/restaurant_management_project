from django.db import models
from account.models import UserProfile
from products.models import Menu


# Create your models here.

class OrderModel(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('CONFIRM', 'Confirm'),
        ('DELIEVERED', 'Delievered'),
        ('CANCELLED', 'Cancelled'),
    ]
    customer = models.ForeignKey(UserProfile, on_delete = models.CASCADE)
    order_item = models.ManyToManyField(Menu)
    total_amount = models.DecimalField(max_digiti = 10, decimal_places=2)
    order_status = models.CharField(max_length=10, choices= STATUS_CHOICES, default='PENDING')
    create_at = models.DAteTimeField(auto_now_add = True)

    defe __str__(self):
        return f"Order #{self.id} by {self.customer.name}"

