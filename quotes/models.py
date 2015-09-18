from django.db import models

# Create your models here.
    
class Author(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Source(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, blank=True, null=True)
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.title

class Quote(models.Model):
    body = models.CharField(max_length=400)
    source = models.ForeignKey(Source, blank=True, null=True)
    
    def __str__(self):
        return self.body