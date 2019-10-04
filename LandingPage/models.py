from django.db import models
from django.conf import settings

# Create your models here.

class Reporter(models.Model):
    full_name = models.CharField(max_length=70)

    def __str__(self):
        return self.full_name


class Article(models.Model):
    cover = models.ImageField(upload_to='images/', null=True)
    reporter = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    published_date = models.DateField()
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title