
from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import *


class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = ('username', 'email', 'name', 'password', 'key')


class answersSerializer(serializers.ModelSerializer):
    class Meta:
        model = answers
        fields = ('id', 'image', 'by', "note")


class questionSerializer(serializers.ModelSerializer):
    answers = answersSerializer(many=True, read_only=True)

    class Meta:
        model = question
        fields = ('id', 'name', 'part', "answers")


class examSerializer(serializers.ModelSerializer):
    questions = questionSerializer(many=True, read_only=True)

    class Meta:
        model = exam
        fields = ('id', 'name', 'questions')


class ErrorSerializer(serializers.Serializer):
    error = serializers.CharField(max_length=200)
