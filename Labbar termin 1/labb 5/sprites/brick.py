from __future__ import annotations
from dataclasses import dataclass
import pygame
from .base import Sprite

@dataclass
class Brick(Sprite):
    hits_left: int
    points: int
    color: tuple[int, int, int]

    def hit(self) -> bool:
        """Returns True if destroyed after this hit."""
        self.hits_left -= 1
        return self.hits_left <= 0

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.rect(screen, self.color, self.rect, border_radius=6)
        pygame.draw.rect(screen, (0, 0, 0), self.rect, width=2, border_radius=6)

def make_soft_brick(rect: pygame.Rect) -> Brick:
    # 1 hit, lower points
    return Brick(rect=rect, hits_left=1, points=50, color=(90, 180, 255))

def make_hard_brick(rect: pygame.Rect) -> Brick:
    # 2 hits, higher points
    return Brick(rect=rect, hits_left=2, points=120, color=(255, 120, 90))
