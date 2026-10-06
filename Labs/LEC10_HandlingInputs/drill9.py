import os

from pico2d import *


open_canvas()
animation_sheet = load_image(
	os.path.join(os.path.dirname(__file__), 'animation_sheet.png')
)
