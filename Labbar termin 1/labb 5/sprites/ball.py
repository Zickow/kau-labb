from __future__ import annotations
from dataclasses import dataclass
import math
import pygame
from .base import Sprite

@dataclass
class Ball(Sprite):
    radius: int
    vel: pygame.Vector2
    color: tuple[int, int, int] = (250, 250, 250)

    def update(self, dt: float) -> None:
        self.rect.x += int(self.vel.x * dt)
        self.rect.y += int(self.vel.y * dt)

    def bounce_x(self) -> None:
        self.vel.x *= -1

    def bounce_y(self) -> None:
        self.vel.y *= -1

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, self.color, self.rect.center, self.radius)
        pygame.draw.circle(screen, (0, 0, 0), self.rect.center, self.radius, width=2)

    def reflect_off_bat(self, bat_rect: pygame.Rect) -> None:
        """Angle bounce based on where the ball hits the bat."""
        hit_pos = (self.rect.centerx - bat_rect.centerx) / (bat_rect.width / 2)
        hit_pos = max(-1.0, min(1.0, hit_pos))
        max_angle = math.radians(65)
        angle = hit_pos * max_angle
        speed = self.vel.length() or 1.0
        self.vel.x = speed * math.sin(angle)
        self.vel.y = -abs(speed * math.cos(angle))
