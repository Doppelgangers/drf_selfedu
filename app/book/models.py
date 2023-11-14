from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    category = models.ForeignKey("Category", on_delete=models.PROTECT, null=True)


    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=64, db_index=True)

    def __str__(self):
        return self.name