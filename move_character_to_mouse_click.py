from pico2d import *

open_canvas()

TUK_WHIDTH, TUK_HEIGHT = 1280, 860
open_canvas(TUK_WHIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
arrow = load_image('hand_arrow.png')


def handle_events():
    global running
    global a_x, a_y, arrow_list

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
                arrow_list.append([event.x, TUK_HEIGHT - 1 - event.y])


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
point_c = [x, y]
arrow_list = [[TUK_WHIDTH, TUK_HEIGHT]]
frame, t = 0, 0

hide_cursor()

while running:
    clear_canvas()

    tuk_ground.draw(TUK_WHIDTH // 2, TUK_HEIGHT // 2)

    arrow.draw(a_x, a_y)

    for i in arrow_list[1:]:
        arrow.draw(i[0], i[1])

    if len(arrow_list) > 1 and arrow_list[1] == [x, y]:
        point_c = [x, y]
        t = 0
        arrow_list.pop(0)

    if len(arrow_list) == 1 or len(arrow_list) > 1 and x < arrow_list[1][0]:
        character.clip_draw(frame * 100, 100, 100, 100, x, y)  # right
    else:
        character.clip_draw(frame * 100, 0, 100, 100, x, y)  # left

    if len(arrow_list) > 1:
        draw_line(point_c, arrow_list[1])

    update_canvas()
    handle_events()

    frame = (frame + 1) % 8

    delay(0.02)

close_canvas()

#code submit
