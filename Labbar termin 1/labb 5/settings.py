from dataclasses import dataclass

@dataclass(frozen=True)
class Settings:
    width: int = 900
    height: int = 600
    fps: int = 60

    bg_color: tuple[int, int, int] = (15, 15, 20)
    text_color: tuple[int, int, int] = (240, 240, 245)

    bat_width: int = 120
    bat_height: int = 18
    bat_speed: float = 520.0

    ball_radius: int = 9
    ball_speed: float = 420.0

    brick_cols: int = 10   # at least 8 required
    brick_rows: int = 5    # at least 3 required
    brick_gap: int = 6
    brick_top_margin: int = 70
    brick_side_margin: int = 40
    brick_height: int = 26

    starting_lives: int = 3
