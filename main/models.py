import uuid
from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('boots', 'Boots'),
        ('jersey', 'Jersey'),
        ('ball', 'Ball'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.CharField(max_length=20)
    thumbnail = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='update')
    is_featured = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
