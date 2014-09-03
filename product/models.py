from django.db import models
import time
def get_upload_file_name(instance, filename):
    return "uploaded_file/%s_%s" % (str(time()), filename)


class Product(models.Model):
    price = models.DecimalField(max_digits=4, decimal_places=2)
    image = models.FileField(upload_to=get_upload_file_name)
    name = models.CharField(max_length=20)
    duration = models.TimeField()
    onstack = models.BooleanField(default=True)

# Create your models here.
