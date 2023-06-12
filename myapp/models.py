from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    enquiry = models.TextField()
    
<<<<<<< HEAD
=======
    
>>>>>>> ee54d6bbf1f307d1232f81e6e392f6d2553c28cf
    def __str__(self):
        return self.name
