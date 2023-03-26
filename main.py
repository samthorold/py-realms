import logging

from models.game import Game


logger = logging.getLogger(__name__)


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    print("Py Realms - a Python implementation of Star Realms")
    game = Game()
    game.play()
