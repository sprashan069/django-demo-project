from django.db import models



class Employee(models.Model):
    name = models.CharField(max_length=50, blank=True)
    email = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=50, blank=True)
    def __str__(self):
        return self.name

# Create your models here.
class File(models.Model):
    file = models.FileField(blank=False, null=False, upload_to="files/")
    name = models.CharField(max_length=50, blank=True)
    def __str__(self):
        return self.file.name