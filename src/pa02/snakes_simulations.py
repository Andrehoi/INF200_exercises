# -*- coding: utf-8 -*-

__author__ = 'sebastian kihle', 'andreas sandvik hoimyr'
__email__ = 'sebaskih@nmbu.no', 'andrehoi@nmbu.no'

import random

class Board:

    def __init__(self, ladders=([1, 40],[9, 11],[37, 53],[44, 63],[50, 80],
                                [66, 83],[69, 86]),
                 chutes=([25, 6],[34, 4],[43, 31],[57, 38],[65, 28],[75, 13],
                         [88,71]), goal=90):
        self.board = []
        for tiles in range(96):
            self.board.append([tiles, 0])
        self.ladders = ladders
        self.chutes = chutes
        self.goal = goal

    def goal_reached(self, *args):
        if args is not None:
            return True
        return not self.board[self.goal][1] == 0

    def position_adjustment(self, position):
        for chute in self.chutes:
            if chute[0] == position:
                return chute[1]

        for ladder in self.ladders:
            if ladder[0] == position:
                return ladder[1]
        return position


class Player:
    def __init__(self, board):
        self.board = board
        self.position = 0

    def move(self):
        thorw_die = random.randint(1, 6)
        self.position += thorw_die
        self.board.position_adjustment(self.position)


class ResilientPlayer(Player):
    def __init__(self, board, extra_steps=1):
        super().__init__(board)
        self.add_move = extra_steps
        self.prev_pos = 0
        self.new_pos = 0

    def move_resilient(self):

        self.position += random.randint(1, 6)

        if self.board.position_adjustment(self.position) < self.position:
            pass


class LazyPlayer(Player):
    def __init__(self, board, dropped_steps=1):
        super().__init__(board)
        self.red_move = dropped_steps

    def move_lazy(self):
        self.position += random.randint(1, 6)
        if self.board.position_adjustment(self.position) > self.position:
            pass


class Simulation:
    def __init__(self, *players, randomize_players=True):
        self.players = [players]
        self.Lazy = LazyPlayer(Board())
        self.Resilient = ResilientPlayer(Board())
        self.play = Player(Board())

    def single_game(self):

        while True:
            for player in self.players:
                player.move()
                player.position_adjustment()
                player.goal_reached()
                if type(player) == type(self.Lazy):



        pass

    def run_simulation(self):
        pass

    def get_results(self):
        pass

    def winners_per_type(self):
        pass

    def durations_per_type(self):
        pass

    def players_per_type(self):
        pass


g = LazyPlayer(Board())
p = ResilientPlayer(Board())
print(type(g))
print(type(p))

