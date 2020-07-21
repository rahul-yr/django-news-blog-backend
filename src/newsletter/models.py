from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Newsletter(models.Model):
    email = models.EmailField(_('email address'), unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    interests = models.TextField(max_length=1024, blank=True,null=True)
    location = models.CharField(max_length=30, null=True,blank=True)

    class Meta:
        ordering = ['-created_on']
        
    def __str__(self):
        return self.email


class ContactForm(models.Model):
    contact_email = models.EmailField(_('email address'),blank=False,null=False)
    created_on = models.DateTimeField(auto_now_add=True)
    title = models.TextField(max_length=1024,blank=False,null=False)
    message = models.TextField(blank=False,null=False)
    location = models.CharField(max_length=50,blank=False,null=False)

    class Meta:
        ordering = ['-created_on']
        
    def __str__(self):
        return self.contact_email