from __future__ import annotations
from dataclasses import dataclass
import pygame

@dataclass
class Sprite:
    """Superclass for visual objects on the game board."""
    rect: pygame.Rect

    def update(self, dt: float) -> None:
        pass

    def draw(self, screen: pygame.Surface) -> None:
        raise NotImplementedError
