from django.db import models

# Models
class Subscribe(models.Model):
    email             = models.EmailField(max_length=100)
    subscription_date = models.DateField(auto_now_add=True)
    def __str__(self):
       return  "Email : " + self.email


class Contact(models.Model):
    full_name         = models.CharField(max_length=300,blank=True, null=True)
    house_number      = models.CharField(max_length=300,blank=True, null=True)
    postcode          = models.IntegerField(blank=True, null=True)
    telephone          = models.IntegerField(blank=True, null=True)
    email             = models.EmailField(max_length=100)
    besttime          = models.CharField(max_length=300, blank=True, null=True)
    services          = models.CharField(max_length=300, blank=True, null=True)
    contact_date      = models.DateField(auto_now_add=True)
    def __str__(self):
       return  "Email : " + self.email


class leads(models.Model):
    name         = models.CharField(max_length=300, blank=True, null=True)
    phone      = models.CharField(max_length=300,blank=True, null=True)
    postcode         = models.CharField(max_length=300,blank=True, null=True)
    email  = models.EmailField(max_length=300,blank=True, null=True)
    def __str__(self):
        return  "Contact_User : " + self.name
