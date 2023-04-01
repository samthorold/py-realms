import logging

from models.game import Game


logger = logging.getLogger(__name__)


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.DEBUG,
        filename="pyrealms.log",
        filemode="w",
        format="%(asctime)s:%(levelname)s:%(name)s:%(funcName)s:%(lineno)s:%(message)s",
    )
    print("Py Realms - a Python implementation of Star Realms")
    game = Game()
    game.action("START_GAME")
    game.action("play", idx=0)
