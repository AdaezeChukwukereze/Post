from django.db import models

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=50)
    content =models.CharField(max_length=500)
    reporter =models.CharField(max_length=50)
    image = models.ImageField(upload_to='img')
    date_reported =models.DateTimeField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural= 'News'
