from django.db import models
from rest_framework import serializers
# Create your models here.
from django.core.signing import Signer
signer = Signer()


class user(models.Model):
    username = models.CharField(max_length=100, unique=True)
    email = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    key = models.CharField(max_length=100)

    def __str__(self):
        return str(self.username)


class user_details(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)


class answers(models.Model):
    image = models.ImageField(upload_to='Answers')
    by = models.CharField(max_length=100)
    note = models.CharField(max_length=800)


class question(models.Model):
    name = models.CharField(max_length=100)
    part = models.CharField(max_length=100)
    answers = models.ManyToManyField(answers)

    def __str__(self):
        return str(self.name)+str(self.part)


class exam(models.Model):
    name = models.CharField(max_length=100, unique=True)
    questions = models.ManyToManyField(question)

    def __str__(self):
        return str(self.name)
