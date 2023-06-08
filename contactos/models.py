from django.db import models
from django.core.exceptions import ValidationError


def validate_only_numbers(value):
    if not value.isdigit():
        raise ValidationError("Este campo solo debe contener números.")

class Contacto(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=15, validators=[validate_only_numbers])
    address = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=50, validators=[validate_only_numbers])
    description = models.TextField(max_length=2000)
    
    def __str__(self):
        return self.name