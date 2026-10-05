"""Play every animation in the Sonic sprite sheet with pico2d."""

from dataclasses import dataclass
from pathlib import Path
from time import perf_counter

from pico2d import (
    SDL_QUIT,
    close_canvas,
    clear_canvas,
    delay,
    get_events,
    load_image,
    open_canvas,
    update_canvas,
)


CANVAS_WIDTH = 1200
CANVAS_HEIGHT = 800
SPRITE_WIDTH = 399
SPRITE_HEIGHT = 525
SPRITE_SCALE = 4
FRAME_DURATION = 0.1
REPEAT_COUNT = 5
REST_DURATION = 1.0
GROUND_Y = 140


@dataclass(frozen=True)
class Frame:
    left: int
    top: int
    width: int
    height: int


@dataclass(frozen=True)
class Animation:
    name: str
    movement: str
    frames: tuple


def _frames_from_bounds(bounds):
    frames = []
    for left, top, right, bottom in bounds:
        crop_left = max(0, left - 1)
        crop_top = max(0, top - 1)
        crop_right = min(SPRITE_WIDTH, right + 2)
        crop_bottom = min(SPRITE_HEIGHT, bottom + 2)
        frames.append(
            Frame(
                crop_left,
                crop_top,
                crop_right - crop_left,
                crop_bottom - crop_top,
            )
        )
    return tuple(frames)


_ANIMATION_DATA = [
    (
        "대기 자세",
        "still",
        [
            (1, 39, 29, 77),
            (31, 40, 56, 77),
            (58, 39, 85, 77),
            (86, 40, 115, 77),
            (118, 40, 147, 77),
            (150, 40, 179, 77),
            (182, 40, 210, 77),
            (211, 39, 239, 76),
            (240, 39, 268, 76),
            (270, 45, 293, 76),
            (302, 51, 330, 76),
        ],
    ),
    (
        "달리기",
        "run",
        [
            (8, 80, 33, 116),
            (37, 80, 63, 116),
            (65, 80, 95, 117),
            (97, 80, 133, 116),
            (135, 80, 166, 114),
            (170, 79, 201, 116),
            (206, 79, 231, 116),
            (238, 80, 261, 116),
            (263, 80, 292, 116),
            (295, 80, 330, 116),
            (334, 80, 365, 115),
            (370, 79, 398, 116),
        ],
    ),
]
ANIMATIONS = tuple(
    Animation(name, movement, _frames_from_bounds(bounds))
    for name, movement, bounds in _ANIMATION_DATA
)
