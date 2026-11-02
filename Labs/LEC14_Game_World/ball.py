from pico2d import load_image, get_canvas_width
import game_world


class Ball:
    def __init__(self, x, y, face_dir):
        self.image = load_image('ball21x21.png')
        self.x = x + face_dir * 30
        self.y = y
        self.face_dir = face_dir

    def update(self):
        self.x += self.face_dir * 10
        if self.x < -25 or self.x > get_canvas_width() + 25:
            game_world.remove_object(self)

    def draw(self):
        self.image.draw(self.x, self.y)
