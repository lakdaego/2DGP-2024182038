import random

from pico2d import get_canvas_width, load_image

import game_framework


FRAME_COUNT = 14
FRAME_RATE = 12
SPRITE_COLUMNS = 5
SPRITE_ROWS = 3


class Bird:
    image = None

    def __init__(self):
        if Bird.image is None:
            Bird.image = load_image('bird_animation.png')

        self.x = random.uniform(get_canvas_width() * 0.2, get_canvas_width() * 0.8)
        self.y = random.uniform(300, 500)
        self.speed = random.uniform(40, 100)
        self.scale = random.uniform(0.6, 0.9)
        self.frame = random.randrange(FRAME_COUNT)

    def update(self):
        frame_time = game_framework.frame_time
        self.x += self.speed * frame_time
        if self.x > get_canvas_width() + 100:
            self.x = -100

        self.frame = (self.frame + FRAME_RATE * frame_time) % FRAME_COUNT

    def draw(self):
        frame = int(self.frame)
        column = frame % SPRITE_COLUMNS
        row = frame // SPRITE_COLUMNS

        image_width = Bird.image.w
        image_height = Bird.image.h
        left = column * image_width // SPRITE_COLUMNS
        right = (column + 1) * image_width // SPRITE_COLUMNS
        bottom = image_height - (row + 1) * image_height // SPRITE_ROWS
        top = image_height - row * image_height // SPRITE_ROWS

        width = right - left
        height = top - bottom
        Bird.image.clip_draw(
            left, bottom, width, height,
            self.x, self.y, width * self.scale, height * self.scale
        )
