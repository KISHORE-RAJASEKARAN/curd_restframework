from django.db import models

class trainer(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    email = models.CharField(max_length=20)
    contact_no = models.CharField(max_length=13)

class trainee(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    email = models.CharField(max_length=20)
    contact_no = models.CharField(max_length=13)

class doubts(models.Model):
    name = models.CharField(max_length=20)
    question = models.CharField(max_length=500)
    answer = models.CharField(max_length=500)
    _from = models.ForeignKey(trainee,on_delete=models.CASCADE)
    _by = models.ForeignKey(trainer, on_delete=models.CASCADE)