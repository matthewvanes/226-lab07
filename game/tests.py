from django.test import TestCase
from game.models import Player
import game.constants

class PlayerTestCase(TestCase):
# 1. No Player with an invalid row (both ends) can be created

	def test_invalid_row_above(self):
		response = self.client.post("/game/player/create/", { 'tag':'T', 'row':13, 'col':7})
		self.assertFormError(response, 'form', 'row', 'Out of range')
	
	def test_invalid_row_below(self):
		response = self.client.post("/game/player/create/", { 'tag':'T', 'row':'-3', 'col':7})
		self.assertFormError(response, 'form', 'row', 'Out of range')
	
# 2. No Player with an invalid column (both ends) can be created

	def test_invalid_col_above(self):
		response = self.client.post("/game/player/create/", { 'tag':'T', 'row':3, 'col':17})
		self.assertFormError(response, 'form', 'col', 'Out of range')
	
	def test_invalid_col_below(self):
		response = self.client.post("/game/player/create/", { 'tag':'T', 'row':'3', 'col':'-7'})
		self.assertFormError(response, 'form', 'col', 'Out of range')

# 3. No Player with a duplicate tag can be created.
	
	def test_duplicate_tags(self):
		self.client.post("/game/player/create/", { 'tag':'T', 'row':3, 'col':3})
		response = self.client.post("/game/player/create/", { 'tag':'T', 'row':3, 'col':3})
		self.assertFormError(response, 'form', 'tag', 'Tag already taken')

# 4. No Player can move to an invalid row (both ends)

	def test_invalid_row_move_above(self):
		self.client.post("/game/player/create/", { 'tag':'T', 'row':9, 'col':9})
		response = self.client.post("/game/player/1/update/", { 'row':10, 'col':9})
	
	def test_invalid_row_move_below(self):
		self.client.post("/game/player/create/", { 'tag':'T', 'row':0, 'col':0})
		response = self.client.post("/game/player/1/update/", { 'row':'-1', 'col':9})

# 5. No Player can move to an invalid column (both ends) 


	def test_invalid_col_move_above(self):
		self.client.post("/game/player/create/", { 'tag':'T', 'row':9, 'col':9})
		response = self.client.post("/game/player/1/update/", { 'row':9, 'col':10})
	
	def test_invalid_col_move_below(self):
		self.client.post("/game/player/create/", { 'tag':'T', 'row':0, 'col':0})
		response = self.client.post("/game/player/1/update/", { 'row':0, 'col':'-1'})
