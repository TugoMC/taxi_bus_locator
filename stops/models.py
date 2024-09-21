from django.db import models

class Stop(models.Model):
    STOP_TYPES = [
        ('taxi', 'Taxi'),
        ('bus', 'Bus'),
    ]
    
    name = models.CharField(max_length=100)
    stop_type = models.CharField(max_length=4, choices=STOP_TYPES)
    start_photo = models.ImageField(upload_to='stops/images/')
    end_photo = models.ImageField(upload_to='stops/images/')
    commune = models.CharField(max_length=50)
    description = models.TextField()
    cost = models.DecimalField(max_digits=8, decimal_places=2)
    opening_time = models.TimeField()
    closing_time = models.TimeField()
    
    def __str__(self):
        return self.name