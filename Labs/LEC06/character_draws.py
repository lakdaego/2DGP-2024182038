# 실습 과제 진행
import os
from pico2d import *

image_path = os.path.join(os.path.dirname(__file__), 'character.png')

open_canvas(800, 600)
character = load_image(image_path)

theta = math.radians(30)
x = 400 + 200 * math.cos(theta)
y = 300 + 200 * math.sin(theta)


def move_circle():
    print("circle")
    clear_canvas()
    character.draw(400, 300)
    update_canvas()

def move_rectangle():
    print("rectangle")

def move_triangle():
    print("triangle")
    pass



while True:
    move_circle()
    move_rectangle()
    move_triangle()
    pass


close_canvas()