from django.db import models
from django.urls import reverse
from datetime import datetime 

class Student(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    enter = models.FloatField(null=True)
    testScore = models.FloatField()
    Amount = models.FloatField(null=True, blank=True)
    date = models.DateTimeField(default=datetime.now, blank=True)

    @property
    def get_price(self):
        a = ((self.enter * self.testScore)/ 100) + self.enter     
        return a 
     
    def save(self, *args, **kwargs):
        self.Amount = self.get_price
        super(Student, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("student")

