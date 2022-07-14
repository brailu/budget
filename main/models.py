from django.db import models

class Category(models.Model):
    
    name = models.TextField(
        blank=False,
        null=False,
        max_length=100
    )

    def clean(self):
        self.name = self.name.upper()


class Account(models.Model):
    
    name = models.TextField(
        blank=False,
        null=False,
        max_length=100
    )

    balance = models.DecimalField(
        blank=False,
        null=False,
        max_digits=11,
        decimal_places=2
    )

    type = models.CharField(
        blank=False,
        null=False,
        max_length=100
    )
    
    def clean(self):
        self.name = self.name.upper()
