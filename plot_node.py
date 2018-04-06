from enum import Enum, auto


# Enumerator for possible event types
class EventType(Enum):
    DEFAULT = auto()
    ENEMY_SHIP_ESCAPE = auto()
    CREW_MEMBER_KILLED = auto()


# Interface for events that a PlotNode can respond to.
class OutputEvent:
    type = EventType.DEFAULT


# Interface for section in the story.
class PlotNode:
    is_visible = False  # Dictates whether or not this node is shown to the player

    def __init__(self, game):
        self.game = game

    def process_event(self):
        pass

    def esc_node(self):
        self.game.set_node(PlotNode(self.game))
