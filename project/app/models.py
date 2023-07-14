from django.db import models

class Student(models.Model):
    fname = models.CharField(max_length=50)   
    
    def __str__(self):
        return self.fname
