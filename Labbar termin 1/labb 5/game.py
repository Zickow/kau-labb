from __future__ import annotations
import random
import pygame

from .settings import Settings
from .sprites.bat import Bat
from .sprites.ball import Ball
from .sprites.brick import Brick, make_soft_brick, make_hard_brick

class Game:
    def __init__(self, settings: Settings) -> None:
        self.s = settings
        self.screen = pygame.display.set_mode((self.s.width, self.s.height))
        pygame.display.set_caption("Breakout (Pygame)")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("consolas", 22)
        self.big_font = pygame.font.SysFont("consolas", 44, bold=True)
        self.reset()

    def reset(self) -> None:
        self.points = 0
        self.lives = self.s.starting_lives
        self.game_over = False
        self.won = False

        bat_rect = pygame.Rect(0, 0, self.s.bat_width, self.s.bat_height)
        bat_rect.center = (self.s.width // 2, self.s.height - 60)
        self.bat = Bat(rect=bat_rect, speed=self.s.bat_speed)

        ball_rect = pygame.Rect(0, 0, self.s.ball_radius * 2, self.s.ball_radius * 2)
        ball_rect.centerx = self.bat.rect.centerx
        ball_rect.bottom = self.bat.rect.top - 2
        self.ball = Ball(rect=ball_rect, radius=self.s.ball_radius, vel=pygame.Vector2(0, 0))
        self.ball_attached = True

        self.bricks: list[Brick] = []
        self._create_bricks()

    def _create_bricks(self) -> None:
        cols = max(8, self.s.brick_cols)
        rows = max(3, self.s.brick_rows)

        total_gap = (cols - 1) * self.s.brick_gap
        usable_w = self.s.width - 2 * self.s.brick_side_margin - total_gap
        brick_w = usable_w // cols

        y = self.s.brick_top_margin
        for r in range(rows):
            x = self.s.brick_side_margin
            for _ in range(cols):
                rect = pygame.Rect(x, y, brick_w, self.s.brick_height)
                brick = make_soft_brick(rect) if r % 2 == 0 else make_hard_brick(rect)
                self.bricks.append(brick)
                x += brick_w + self.s.brick_gap
            y += self.s.brick_height + self.s.brick_gap

    def _launch_ball(self) -> None:
        vx = random.choice([-1, 1]) * (self.s.ball_speed * 0.55)
        vy = -self.s.ball_speed
        self.ball.vel = pygame.Vector2(vx, vy)
        self.ball_attached = False

    def _reset_ball_on_bat(self) -> None:
        self.ball_attached = True
        self.ball.vel = pygame.Vector2(0, 0)
        self.ball.rect.centerx = self.bat.rect.centerx
        self.ball.rect.bottom = self.bat.rect.top - 2

    def handle_events(self) -> bool:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False
                if event.key == pygame.K_SPACE and (not self.game_over) and self.ball_attached:
                    self._launch_ball()
                if event.key == pygame.K_r and self.game_over:
                    self.reset()
        return True

    def update(self, dt: float) -> None:
        keys = pygame.key.get_pressed()
        direction = 0.0
        if keys[pygame.K_LEFT]:
            direction -= 1.0
        if keys[pygame.K_RIGHT]:
            direction += 1.0
        self.bat.move(direction, dt, 0, self.s.width)

        if self.ball_attached:
            self.ball.rect.centerx = self.bat.rect.centerx
            self.ball.rect.bottom = self.bat.rect.top - 2
            return

        self.ball.update(dt)

        # Walls: left/right/top
        if self.ball.rect.left <= 0:
            self.ball.rect.left = 0
            self.ball.bounce_x()
        if self.ball.rect.right >= self.s.width:
            self.ball.rect.right = self.s.width
            self.ball.bounce_x()
        if self.ball.rect.top <= 0:
            self.ball.rect.top = 0
            self.ball.bounce_y()

        # Bottom: lose life (no wall)
        if self.ball.rect.top >= self.s.height:
            self.lives -= 1
            if self.lives <= 0:
                self.game_over = True
                self.won = False
            self._reset_ball_on_bat()
            return

        # Bat collision only when falling
        if self.ball.vel.y > 0 and self.ball.rect.colliderect(self.bat.rect):
            self.ball.rect.bottom = self.bat.rect.top - 1
            self.ball.reflect_off_bat(self.bat.rect)

        # Brick collision (one per frame)
        idx = self.ball.rect.collidelist([b.rect for b in self.bricks])
        if idx != -1:
            brick = self.bricks[idx]

            overlap_left = self.ball.rect.right - brick.rect.left
            overlap_right = brick.rect.right - self.ball.rect.left
            overlap_top = self.ball.rect.bottom - brick.rect.top
            overlap_bottom = brick.rect.bottom - self.ball.rect.top
            min_overlap = min(overlap_left, overlap_right, overlap_top, overlap_bottom)

            destroyed = brick.hit()
            if destroyed:
                self.points += brick.points
                self.bricks.pop(idx)
            else:
                brick.color = (max(0, brick.color[0]-40),
                               max(0, brick.color[1]-40),
                               max(0, brick.color[2]-40))

            if min_overlap in (overlap_left, overlap_right):
                self.ball.bounce_x()
            else:
                self.ball.bounce_y()

            if not self.bricks:
                self.game_over = True
                self.won = True

    def draw(self) -> None:
        self.screen.fill(self.s.bg_color)

        for b in self.bricks:
            b.draw(self.screen)
        self.bat.draw(self.screen)
        self.ball.draw(self.screen)

        hud = self.font.render(f"Points: {self.points}    Lives: {self.lives}",
                               True, self.s.text_color)
        self.screen.blit(hud, (16, 16))

        if self.game_over:
            msg = "YOU WIN!" if self.won else "GAME OVER"
            txt = self.big_font.render(msg, True, self.s.text_color)
            sub = self.font.render("Press R to restart", True, self.s.text_color)
            self.screen.blit(txt, txt.get_rect(center=(self.s.width//2, self.s.height//2 - 20)))
            self.screen.blit(sub, sub.get_rect(center=(self.s.width//2, self.s.height//2 + 28)))
        elif self.ball_attached:
            tip = self.font.render("Press SPACE to launch", True, self.s.text_color)
            self.screen.blit(tip, tip.get_rect(center=(self.s.width//2, self.s.height - 20)))

        pygame.display.flip()

    def run(self) -> None:
        while True:
            dt = self.clock.tick(self.s.fps) / 1000.0
            if not self.handle_events():
                break
            if not self.game_over:
                self.update(dt)
            self.draw()
