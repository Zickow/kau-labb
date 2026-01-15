import pygame
from .settings import Settings
from .game import Game

def main() -> None:
    pygame.init()
    try:
        Game(Settings()).run()
    finally:
        pygame.quit()

if __name__ == "__main__":
    main()
