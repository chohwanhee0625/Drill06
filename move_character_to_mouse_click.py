from pico2d import *
from random import *

open_canvas()

TUK_WHIDTH, TUK_HEIGHT = 1280, 860
open_canvas(TUK_WHIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
arrow = load_image('hand_arrow.png')


def handle_events():
    global running, a_x, a_y, p_h
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            a_x, a_y = event.x, TUK_HEIGHT - 1 - event.y
        elif event.type == SDL_MOUSEBUTTONDOWN:
            if event.button == SDL_BUTTON_LEFT:
                p_h[0], p_h[1] = event.x, TUK_HEIGHT - 1 - event.y

def draw_line(p1, p2):
    global t, x, y

    x1, y1 = p1[0], p1[1]
    x2, y2 = p2[0], p2[1]

    t += 2
    x = (1 - t / 100) * x1 + t / 100 * x2
    y = (1 - t / 100) * y1 + t / 100 * y2



running = True
x, y = TUK_WHIDTH // 2, TUK_HEIGHT // 2
a_x, a_y = TUK_WHIDTH // 2, TUK_HEIGHT // 2
p_c = [x, y]
p_h = [randint(0, TUK_WHIDTH), randint(0, TUK_HEIGHT)]
frame = 0
t = 0

hide_cursor()

while running:
    clear_canvas()

    tuk_ground.draw(TUK_WHIDTH // 2, TUK_HEIGHT // 2)

    if x == p_h[0] and y == p_h[1]:
        #p_h[0], p_h[1] = randint(0, TUK_WHIDTH), randint(0, TUK_HEIGHT)
        p_c = [x, y]
        t = 0

    arrow.draw(p_h[0], p_h[1])

    arrow.draw(a_x, a_y)

    if p_c[0] <= p_h[0]:
        character.clip_draw(frame * 100, 100, 100, 100, x, y)  # right
    else:
        character.clip_draw(frame * 100, 0, 100, 100, x, y)  # left

    draw_line(p_c, p_h)

    update_canvas()
    handle_events()

    frame = (frame + 1) % 8

    delay(0.02)

close_canvas()
