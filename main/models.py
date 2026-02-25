from django.db import models



class Students(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField(default=5)
    is_active = models.BooleanField(default=True)
    birth_date = models.DateField(blank=True,null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

