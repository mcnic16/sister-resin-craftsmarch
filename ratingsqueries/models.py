from django.db import models
from products.models import Product
from django.contrib.auth.models import User

RATING = (
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
) 


class ProductReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    review = models.TextField(max_length=500, blank=True)
    product_rating = models.CharField(choices=RATING, max_length=150)
