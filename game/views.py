from django.shortcuts import render
from django.http import HttpResponse
from game.models import Player, PlayerEncoder
import game.constants
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
import json

# Create your views here.
def index(request):
	return HttpResponse("Hello world!")

def get_player(request, id):
    player = Player.objects.filter(id=id)
    if (len(player) == 1):
        return HttpResponse(json.dumps(player[0], cls=PlayerEncoder))
    else:
        return HttpResponse("No such player")

def all_players(request):
    players = Player.objects.all()
    if (len(players) > 0):
        return HttpResponse(json.dumps(list(players), cls=PlayerEncoder))
    else:
        return HttpResponse("No players exist")

class PlayerCreate(CreateView):
     model = Player
     fields = '__all__'
     success_url = reverse_lazy('players')
        

class PlayerUpdate(UpdateView):
    model = Player
    fields = ['row', 'col']
    success_url = reverse_lazy('players')

def get_game(request):
    board = [['*']*game.constants.MAX_COLS for i in range(game.constants.MAX_ROWS)]
    for player in Player.objects.all():
        board[player.row][player.col] = player.tag
    return HttpResponse(json.dumps(board))
