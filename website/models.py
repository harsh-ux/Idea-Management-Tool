from os import name
from django.db import models

# Create your models here.
class StickyNotes(models.Model):
    note_title = models.CharField(max_length=255)    
    note_body = models.TextField()  
