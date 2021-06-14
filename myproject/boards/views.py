from django.shortcuts import render
from django.http import HttpResponse
from .models import Board


def home(request):
    boards= Board.objects.all()
    return render(request, 'home.html', {'boards': boards})


def board_topics(request, ):
    board = Board.objects.get(pk=1)
    return render(request, 'topics.html', {'board': board})