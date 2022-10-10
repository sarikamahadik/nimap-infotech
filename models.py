from django.db import models

# Create your models here.
class Hope(models.Model):
    client_id = models.IntegerField()
    client_name = models.CharField(max_length=100)
    created_at = models.DateTimeField()
    created_by = models.CharField(max_length=100)
    def __str__(self):
        return self.client_name