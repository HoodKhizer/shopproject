from django.db import models

# Create your models here.
class LU_Status(models.Model):
    status_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)


class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=300)
    status = models.ForeignKey(LU_Status, on_delete=models.DO_NOTHING)

