from numpy import random

class Dice:
    def __init__(self):
        self._face_value_1 = None
        self._face_value_2 = None

    def roll(self):
        self._face_value_1 = random.choice([1, 2, 3, 4, 5, 6])
        self._face_value_2 = random.choice([1, 2, 3, 4, 5, 6])

        return self._face_value_1 + self._face_value_2

    def rolled_doubles(self):
        if self._face_value_1 == None or self._face_value_2 == None:
            raise RuntimeError ("You have to roll the dice first.")

        return self._face_value_1 == self._face_value_2

class Player:
    def __init__(self, name):
        self._name = name
        
    def get_name(self):
        return self._name

class Box:
    def __init__(self):
        self._landing_count = 0

    def land(self):
        self._landing_count += 1

    def get_landing_count(self):
        return self._landing_count

class JailBox(Box):
    pass

class CommunityChestBox(Box):
    pass

class ChanceBox(Box):
    pass

class PropertyBox(Box):
    pass

class StartBox(Box):
    pass

class FreeParkingBox(Box):
    pass

class GoToJailBox(Box):
    pass

class Board:
    def __init__(self):
        self._board = []
        self._setup_board()

    def _setup_board(self):
        self._board = [Box() for i in range(40)]
        self._board[0] = StartBox()
        self._board[2] = CommunityChestBox()
        self._board[10] = JailBox()
        self._board[17] = CommunityChestBox()
        self._board[20] = FreeParkingBox()
        self._board[22] = ChanceBox()
        self._board[30] = GoToJailBox()
        self._board[33] = CommunityChestBox()
        self._board[36] = ChanceBox()
        

class MonopolySim:
    def __init__(self, n_players):
        self._number_of_players = n_players
        self._board = []
        self._setup_game()

    def _setup_game(self):
        self._board = []