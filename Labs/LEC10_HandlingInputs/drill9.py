import os

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
frame = 0
facing = 1


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
				facing = -1
			elif event.key == SDLK_RIGHT:
				pressed_keys.add(SDLK_RIGHT)
				facing = 1
		elif event.type == SDL_KEYUP:
			if event.key in (SDLK_LEFT, SDLK_RIGHT):
				pressed_keys.discard(event.key)


while running:
	handle_events()

	if SDLK_LEFT in pressed_keys and SDLK_RIGHT in pressed_keys:
		direction = facing
	elif SDLK_LEFT in pressed_keys:
		direction = -1
	elif SDLK_RIGHT in pressed_keys:
		direction = 1
	else:
		direction = 0

	if direction != 0:
		facing = direction
		x = max(50, min(750, x + direction * 5))
		frame = (frame + 1) % 8
	else:
		frame = 0

	clear_canvas()
	background.draw(400, 300, 800, 600)
	source_y = 100 if facing == 1 else 0
	animation_sheet.clip_draw(frame * 100, source_y, 100, 100, x, 100)
	update_canvas()
	delay(0.05)

close_canvas()
