from  django.db import models

class Customer(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 100) 
    email = models.EmailField(max_length = 100)
    phone = models.CharField(max_length = 20)
    address = models.CharField(max_length = 200)

    def __str__(self):
        return str(self.id)

class Interaction(models.Model);
    CHANNEL_CHOICES = [
        ('phone','Phone'),
        ('sms','Sms'),
        ('email','Email'),
        ('letter','Letter'),
     ]
     DIRECTIONS_CHOICES = [
        ('inbound','Inbound'),
        ('outbound,Outbound'),
     ]

     customer = models.ForeinKey(Customer,on_delete=models.CASCADE)
     channel = models.CharField(max_length = 15, choices = CHANNEL_CHOICES ) 
     direction = models.CharField(max_length = 10, choices = DIRECTIONS_CHOICES  )
     interaction_date = models.DateField(auto_now_add=True) 
     summary = models.TextField() 
