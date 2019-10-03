from django.db import models

# Create your models here.
class Document(models.Model):
    name = models.CharField(max_length=5000)
    description = models.TextField()
    num=models.CharField(max_length=50,default=True)
 
    def __unicode__(self):
        return self.name
