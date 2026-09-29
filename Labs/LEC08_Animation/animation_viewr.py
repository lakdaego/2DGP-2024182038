from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('sonic-sprite.png')

frame = 0

for x in range(800, 0, -5):
	clear_canvas()
	grass.draw(400, 30)
	frame_width = 39 if frame == 9 else 40
	character.clip_draw(frame * 40, 405, frame_width, 43, x, 69)
	update_canvas()

	frame = (frame + 1) % 10
	delay(0.05)

close_canvas()

