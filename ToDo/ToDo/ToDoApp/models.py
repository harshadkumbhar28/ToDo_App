from django.db import models


# Create your models here.

class todo(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Completed', 'Completed')
    )
    Title = models.CharField(max_length=50)
    Description = models.TextField(max_length=100)
    Date = models.CharField(max_length=20)
    Status = models.CharField(max_length=20, choices=STATUS)

    def __str__(self):
        return self.Title
