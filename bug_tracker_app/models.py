from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime, timezone

class CustomUserModel(AbstractUser):
    bio = models.CharField(max_length=100)
    def __str__(self):
        return self.username


class TicketModel(models.Model):
    STATUS_OF_TICKETS_CHOICES = [
        ('New', 'New'),
        ('In Porgress', 'In Porgress'),
        ('Done', 'Done'),
        ('Invalid', 'Invalid'),    
    ]
    title = models.CharField(max_length=100)
    time_submitted = models.DateTimeField(auto_now_add=True)
    description = models.TextField(max_length=300)
    status = models.CharField(max_length=20,default=None,choices=STATUS_OF_TICKETS_CHOICES)
    user_filed = models.ForeignKey(CustomUserModel,on_delete=models.CASCADE,null=True,related_name = 'user_filed')
    user_assigned = models.ForeignKey(CustomUserModel,on_delete=models.CASCADE,null=True,related_name = 'user_assigned')
    user_ticket_completed = models.ForeignKey(CustomUserModel,on_delete=models.CASCADE,null=True,related_name = 'user_ticket_completed')
    def __str__(self):
        return self.title
    @property
    def age(self):      
        date_in_datebase = self.time_submitted
        current_date = datetime.now(timezone.utc)
        diffencce_date = current_date - date_in_datebase
        return diffencce_date.days


 







