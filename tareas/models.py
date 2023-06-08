from django.db import models

# Create your models here.
class Tarea(models.Model):
    name = models.CharField(max_length=50)
    date_to_complete = models.DateField(auto_now=False, auto_now_add=False)
    description = models.TextField(max_length=2000)
    priority = models.IntegerField(choices=((1, '1'),(2, '2'),(3, '3'),(4, '4'),(5, '5')))
    
    def __str__(self):
        return self.name