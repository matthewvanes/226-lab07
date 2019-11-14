from django.urls import path
from . import views

urlpatterns = [
	path('', views.get_game, name='players'),
	path('player/<int:id>/', views.get_player, name='player'),
	path('player/create/', views.PlayerCreate.as_view(), name='player_create'),
	path('player/<int:pk>/update/', views.PlayerUpdate.as_view(), name='player_update'),
	path('players/', views.all_players, name ='players'),
	]
