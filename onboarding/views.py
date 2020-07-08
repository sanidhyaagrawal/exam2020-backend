from rest_framework.views import exception_handler
from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
import secrets
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from onboarding.models import *
from onboarding.serializers import *

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.utils.crypto import get_random_string
from django.core.signing import Signer
signer = Signer()


# Create your views here.


@api_view(['POST'])
def signup(request):
    print('signup')
    """eventsSerializer
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        return Response(status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'POST':
        data = request.data
        if user.objects.filter(username=data['username']).exists():
            return Response({'error': 'Username Already Exists'}, status=status.HTTP_406_NOT_ACCEPTABLE)

        user_name = user.objects.create(
            username=data['username'], email=data['email'], password=data['password'], name=data['name'])
        user_name.key = signer.sign(user_name.pk).split(':')[1]
        user_name.save()
        serializer = userSerializer([user_name, user_name], many=True)
        print(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['POST', 'GET'])
def exampaper(request, name):
    print('signup')
    """eventsSerializer
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        ex = exam.objects.get(name)
        serializer = userSerializer([ex, ex], many=True)
        print(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    elif request.method == 'POST':
        data = request.data
        if exam.objects.filter(name=data['name']).exists():
            return Response({'error': 'Username Already Exists'}, status=status.HTTP_406_NOT_ACCEPTABLE)
        ex = exam.objects.create(name=data['name'])

        a = data['paper']
        b = a.split(',')
        for j in b:
            if j.isnumeric():
                num = str(j)
                name = ''
                for i in b[b.index(j)+1:]:
                    if not i.isnumeric():
                        name = num + str(i)
                        que = question.objects.create(name=num, part=str(i))
                        ex.questions.add(que)
                    else:
                        break
            if name == '':
                que = question.objects.create(name=num)
                ex.questions.add(que)
        ex.save()
        print(ex.questions.all())
        return Response(status=status.HTTP_201_CREATED)


@api_view(['POST'])
def postexampaper(request):
    print('signup')
    """eventsSerializer
    List all code snippets, or create a new snippet.
    """

    if request.method == 'POST':
        data = request.data
        if exam.objects.filter(name=data['name']).exists():
            return Response({'error': 'Username Already Exists'}, status=status.HTTP_406_NOT_ACCEPTABLE)
        ex = exam.objects.create(name=data['name'])

        a = data['paper']
        b = a.split(',')
        for j in b:
            if j.isnumeric():
                num = str(j)
                name = ''
                for i in b[b.index(j)+1:]:
                    if not i.isnumeric():
                        name = num + str(i)
                        que = question.objects.create(name=num, part=str(i))
                        ex.questions.add(que)
                    else:
                        break
            if name == '':
                que = question.objects.create(name=num)
                ex.questions.add(que)
        ex.save()
        print(ex.questions.all())
        return Response(status=status.HTTP_201_CREATED)


@api_view(['GET'])
def getexampaper(request, name):
    if request.method == 'GET':
        name.replace('%20', ' ')
        ex = exam.objects.get(name=name)
        serializer = examSerializer([ex, ex], many=True)
        print(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def answer(request):
    if request.method == 'POST':
        data = request.data
        que = question.objects.get(pk=data['qid'])
        answer = answers.objects.create(
            image=data['image'], note=data['note'], by=data['name'])
        que.answers.add(answer)
        que.save()
        return Response(status=status.HTTP_201_CREATED)


@api_view(['GET'])
def getanswers(request, id):
    if request.method == 'GET':
        data = request.data
        que = question.objects.get(pk=id)
        serializer = questionSerializer([que, que], many=True)
        print(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
