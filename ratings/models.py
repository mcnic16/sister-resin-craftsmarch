from django.db import models
from products.models import Product
from django.contrib.auth.models import User


class ReviewRating(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(max_length=500, blank=True)
    rating = models.FloatField()
    
    def __str__(self):
        return self.comment

    






