from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=80)
    image = models.URLField()
    def __str__(self):
        return f'Category: {self.name}'

class Todo(models.Model):
    title = models.CharField(max_length=80)
    details = models.CharField(max_length=300)
    has_been_done = models.BooleanField(default=False)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_completion = models.DateTimeField(blank = True,null = True)
    deadline_date = models.DateTimeField(auto_now_add=False)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)