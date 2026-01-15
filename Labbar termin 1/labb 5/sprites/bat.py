from __future__ import annotations
from dataclasses import dataclass
import pygame
from .base import Sprite

@dataclass
class Bat(Sprite):
    speed: float
    color: tuple[int, int, int] = (230, 230, 230)

    def move(self, direction: float, dt: float, min_x: int, max_x: int) -> None:
        """Move bat horizontally. direction in [-1, 1]."""
        self.rect.x += int(direction * self.speed * dt)
        if self.rect.left < min_x:
            self.rect.left = min_x
        if self.rect.right > max_x:
            self.rect.right = max_x

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.rect(screen, self.color, self.rect, border_radius=8)
