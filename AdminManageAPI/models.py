from django.db import models
from datetime import datetime


class Asset(models.Model):
    name = models.CharField(max_length=100)
    tag = models.CharField(max_length=30)
    properties = models.CharField(max_length=100, blank=True, null=True)
    created_on= models.DateTimeField(default=datetime.now())
    updated_on=models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.name






class Activity(models.Model):
    FREQUENCY_TYPE = (
        ('H', 'Hourly'),
        ('D', 'Daily'),
        ('W', 'Weekly'),
        ('M', 'Monthly'),
        ('Y', 'Yearly'),

    

    )
    name = models.CharField(max_length=100)
    frequency = models.CharField(max_length=30,choices= FREQUENCY_TYPE)
    created_on= models.DateTimeField(default=datetime.now())
    updated_on=models.DateTimeField(default=datetime.now())
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name





class Worker(models.Model):
    name = models.CharField(max_length=100)
    skills = models.CharField(max_length=100)
    phone = models.BigIntegerField(max_length=10, blank=True, null=True)
    created_on= models.DateTimeField(default=datetime.now())
    updated_on=models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.name




class TaskAssign(models.Model):
    task = models.ForeignKey(Activity,on_delete=models.CASCADE)
    asset = models.ForeignKey(Asset,on_delete=models.CASCADE)
    worker=models.ForeignKey(Worker,on_delete=models.CASCADE)

    
    timeOfAllocation= models.DateTimeField(default=datetime.now())
    timeToComplete=models.DateTimeField(default=datetime.now())
    
    def __str__(self):
        return str(self.task) +" "+ str(self.asset)






    



    