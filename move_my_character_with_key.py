from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024

open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk = load_image('TUK_GROUND.png')
character = load_image('spritesheets.png')


def handle_events():
   pass


running = True
frame = 0
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2

# fill here
while running:
    clear_canvas()
    tuk.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)

    update_canvas()
    handle_events()

    frame = (frame + 1) % 8
    delay(0.05)

close_canvas()

