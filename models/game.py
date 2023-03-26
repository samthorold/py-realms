from models.card import Card
from models.deck import Deck
from models.player import Player


# Stronger / more useful typedef would be 3 / 5 scouts or vipers
Player1StartingHand = tuple[Card, Card, Card]
Player2StartingHand = tuple[Card, Card, Card, Card, Card]


def starting_hands(player_starting_deck: list[Card]) -> tuple[Player1StartingHand, Player2StartingHand]:
    """Create the starting hands for each player."""

class Game:
    """Orchestrate the Deck and Players."""

    def __init__(self) -> None:
        self.deck = Deck()
        self.players = [Player(name="P1"), Player(name="P2")]
