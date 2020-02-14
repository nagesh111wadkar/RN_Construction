from django.db import models

# Create your models here.


class ContactForm(models.Model):
    name = models.CharField(max_length=5000)
    emailId = models.EmailField(max_length=5000)
    subject = models.CharField(max_length=5000)
    message = models.CharField(max_length=5000)

    def __str__(self):
        return self.name





