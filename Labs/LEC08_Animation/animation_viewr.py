from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('SamuraiSheet.png')

frame = 0

for _ in range(160):
	clear_canvas()
	grass.draw(400, 30)
	character.clip_draw(frame * 128, 1024, 128, 128, 400, 300)
	update_canvas()

	frame = (frame + 1) % 8
	delay(0.05)

close_canvas()




