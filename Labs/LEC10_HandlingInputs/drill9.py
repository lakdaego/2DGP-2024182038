import os
from math import pi, sqrt

from pico2d import *


open_canvas()
animation_sheet = load_image(
	os.path.join(os.path.dirname(__file__), 'animation_sheet.png')
)
background = load_image(
	os.path.join(os.path.dirname(__file__), 'TUK_GROUND.png')
)

running = True
pressed_keys = set()
x = 400
y = 100
frame = 0
facing = 'right'


def handle_events():
	global running, facing

	for event in get_events():
		if event.type == SDL_QUIT:
			running = False
		elif event.type == SDL_KEYDOWN:
			if event.key == SDLK_ESCAPE:
				running = False
			elif event.key == SDLK_LEFT:
				pressed_keys.add(SDLK_LEFT)
				facing = 'left'
			elif event.key == SDLK_RIGHT:
				pressed_keys.add(SDLK_RIGHT)
				facing = 'right'
			elif event.key == SDLK_UP:
				pressed_keys.add(SDLK_UP)
				facing = 'up'
			elif event.key == SDLK_DOWN:
				pressed_keys.add(SDLK_DOWN)
				facing = 'down'
		elif event.type == SDL_KEYUP:
			if event.key in (SDLK_LEFT, SDLK_RIGHT, SDLK_UP, SDLK_DOWN):
				pressed_keys.discard(event.key)


while running:
	handle_events()

	direction_x = 0
	direction_y = 0
	if SDLK_LEFT in pressed_keys:
		direction_x = -1
	if SDLK_RIGHT in pressed_keys:
		direction_x = 1
	if SDLK_UP in pressed_keys:
		direction_y = 1
	if SDLK_DOWN in pressed_keys:
		direction_y = -1

	if direction_x != 0 or direction_y != 0:
		if direction_y > 0:
			facing = 'up'
		elif direction_y < 0:
			facing = 'down'
		elif direction_x < 0:
			facing = 'left'
		else:
			facing = 'right'

		if direction_x != 0 and direction_y != 0:
			direction_x /= sqrt(2)
			direction_y /= sqrt(2)
		x = max(50, min(750, x + direction_x * 5))
		y = max(50, min(550, y + direction_y * 5))
		frame = (frame + 1) % 8
	else:
		frame = 0

	clear_canvas()
	background.draw(400, 300, 800, 600)
	if facing == 'left':
		source_y = 0
		angle = 0
	elif facing == 'up':
		source_y = 100
		angle = pi / 2
	elif facing == 'down':
		source_y = 100
		angle = -pi / 2
	else:
		source_y = 100
		angle = 0
	animation_sheet.clip_composite_draw(
		frame * 100, source_y, 100, 100, angle, '', x, y, 100, 100
	)
	update_canvas()
	delay(0.05)

close_canvas()
