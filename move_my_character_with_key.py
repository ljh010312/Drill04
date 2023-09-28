from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1024, 800

class Sprite:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

move_right = (
    Sprite(36, 726, 21, 38),
    Sprite(65, 726, 25, 37),
    Sprite(93, 726, 30, 36),
    Sprite(125, 726, 23, 36),
    Sprite(155, 726, 18, 38),
    Sprite(177, 726, 27, 36),
    Sprite(206, 726, 28, 36),
    Sprite(239, 316, 24, 37)
)
move_idle = (
    Sprite(32, 874, 35, 37),
    Sprite(67, 874, 35, 37),
    Sprite(102, 874, 35, 37),
    Sprite(137, 874, 35, 37),
)

open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk = load_image('TUK_GROUND.png')
character = load_image('spritesheets.png')


def handle_events():
    global running, h_dir

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False
            elif event.key == SDLK_RIGHT:
                h_dir += 1
            elif event.key == SDLK_LEFT:
                h_dir -= 1
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                h_dir -= 1
            elif event.key == SDLK_LEFT:
                h_dir += 1
def character_move():
    global running, h_dir, frame, x,y

    if h_dir == 1:
        character.clip_draw(move_right[frame].x, move_right[frame].y, move_right[frame].w, move_right[frame].h , x, y)
        frame = (frame + 1) % 8
        x += h_dir * speed
        if x > TUK_WIDTH:
            x -= speed
    elif h_dir == 0:
        frame = (frame + 1) % 4
        character.clip_draw(move_idle[frame].x, move_idle[frame].y, move_idle[frame].w, move_idle[frame].h, x, y)
    elif h_dir == -1:
        character.clip_composite_draw(move_right[frame].x, move_right[frame].y, move_right[frame].w, move_right[frame].h, 0, 'h', x, y, move_right[frame].w, move_right[frame].h)
        frame = (frame + 1) % 8
        x += h_dir * speed
        if x < 0:
            x += speed



running = True
h_dir = 0
frame = 0
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
speed = 10

# fill here
while running:
    clear_canvas()
    tuk.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    character_move()
    update_canvas()
    handle_events()

    frame = (frame + 1) % 8
    delay(0.05)

close_canvas()

