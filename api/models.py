from msilib.schema import Class
from django.db import models

# Create your models here.
Class Board(models.Model):
    Board_id = models.PositiveIntegerField(primary_key=True),
    name = models.CharField(max_length=100, unique=True),
    Created_date = models.DateTimeField(auto_now_add=True),
    description = models.TextField(),
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField()

    def __str__(self):
        return str(self.Board_id)+" "+self.name
