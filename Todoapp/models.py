from django.contrib.auth.models import User
from django.db import models

class Plan(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    date = models.DateField()
    status = models.CharField(max_length=15,choices=[('new','new'),('finished',"finished")])
    user  =models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.title} ({self.status})"
    def newga_ozgartir(self):
        self.status = 'new'
        self.save()
    def finishedga_ozgartir(self):
        self.status = 'finished'
        self.save()
