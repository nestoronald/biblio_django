from django.db import models

# Create your models here.

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    isbn = models.CharField(max_length=70)
    def __unicode__(self):
        return self.title

