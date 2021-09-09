from django.db import models
import datetime


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.name


class Story(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    name = models.CharField(max_length=250, unique=True)
    author = models.CharField(max_length=250)
    url = models.URLField(null=True)
    content = models.TextField()
    image = models.ImageField(upload_to='stories', default='stories/images/default.png')
    public_day = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.name
