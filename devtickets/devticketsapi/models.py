from django.db import models


# Create your models here.
class Ticket(models.Model):
    type = models.CharField(max_length=10)
    title = models.CharField(max_length=60)
    description = models.CharField(max_length=100)

    def __str__(self):
        ticket_str = f'type: {self.type}, title: {self.title}, description: {self.description}'
        return ticket_str
