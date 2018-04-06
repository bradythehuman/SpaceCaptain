# Game singlton class used to encapsulate all aspects of a save game
class Game:
    def __init__(self):
        self.plot_node =
        self.states = []

    def process_event(self):
        pass

    def set_node(self, node):
        self.plot_node = node


# Interface for the state of the game. Handles open menus, game board, etc.
class State:
    console = ["This is the default state."]

    def __init__(self):
        pass

    def process_event(self):
        pass

    def display(self):
        pass
