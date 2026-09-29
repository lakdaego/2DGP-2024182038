from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('SamuraiSheet.png')

while True:
	for source_y in (1024, 896):
		frame = 0
		for _ in range(60):
			clear_canvas()
			grass.draw(400, 30)
			character.clip_draw(frame * 128, source_y, 128, 128, 400, 300)
			update_canvas()

			frame = (frame + 1) % 8
			delay(0.05)

	for _ in range(10):
		for frame in range(6):
			clear_canvas()
			grass.draw(400, 30)
			character.clip_draw(frame * 128, 640, 128, 128, 400, 300, 154, 154)
			update_canvas()
			delay(0.05)

	for death_frame in range(30):
		clear_canvas()
		grass.draw(400, 30)
		character.clip_draw((death_frame % 3) * 128, 0, 128, 128, 400, 300)
		update_canvas()
		delay(0.1)





