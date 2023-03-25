from models.deck import Deck
from models.player import Player


class Game:
    """Orchestrate the Deck and Players."""

    def __init__(self):
        self.deck = Deck()
        self.players = [Player(name="P1"), Player(name="P2")]
