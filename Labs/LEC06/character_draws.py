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
   for degree in range(360):
        theta = math.radians(degree)
        x = 400 + 200 * math.cos(theta)
        y = 300 + 200 * math.sin(theta)

        clear_canvas()
        character.draw(x, y)
        update_canvas()
        delay(0.01)


def draw_top():
        pass    

def draw_left():    
        pass

def draw_bottom():
        pass

def draw_right():
        pass



def move_rectangle():
    print("rectangle")
    draw_top()
    draw_left()
    draw_bottom()
    draw_right()

def move_triangle():
    print("triangle")
    pass



while True:
    move_circle()
    move_rectangle()
    move_triangle()
    pass


close_canvas()