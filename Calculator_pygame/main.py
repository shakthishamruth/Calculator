import pygame

pygame.init()

# Window
screen = pygame.display.set_mode((800, 675))
pygame.display.set_caption('Calculator')
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)
background = pygame.image.load('background.png')

# Cal output
font = pygame.font.Font('freesansbold.ttf', 64)
eq = ''
a = ''
textX = 26
textY = 20

x = 0
y = 0

input_state = True
running = True


# Functions
def show_cal(x, y):
    global eq
    cal = font.render(str(eq), True, (255, 255, 255))
    screen.blit(cal, (x, y))


def show_ans(x, y):
    global a
    ans = font.render(str(f'= {a}'), True, (255, 255, 255))
    screen.blit(ans, (x, y))


def input_num(x):
    global input_state, eq, a
    if not input_state:
        input_state = True
        eq = f'{x}'
        a = ''
    elif input_state:
        eq += f'{x}'


def input_oper(x):
    global input_state, eq, a
    if not input_state:
        input_state = True
        eq = ''
        a = ''
    elif input_state:
        eq += f'{x}'


def mouse_input(x1, x2, y1, y2, z):
    global x, y, input_state, eq, a
    if x1 < x < x2 and y1 < y < y2:
        if not input_state:
            input_state = True
            eq = f'{z}'
            a = ''
        elif input_state:
            eq += f'{z}'


def mouse_input_oper(x1, x2, y1, y2, z):
    global x, y, input_state, eq, a
    if x1 < x < x2 and y1 < y < y2:
        if not input_state:
            input_state = True
            eq = ''
            a = ''
        elif input_state:
            eq += f'{z}'


def mouse_input_backspace(x1, x2, y1, y2):
    global x, y, input_state, eq, a
    if x1 < x < x2 and y1 < y < y2:
        if not input_state:
            input_state = True
            eq = ''
            a = ''
        elif input_state:
            eq = f'{eq[:-1]}'


def mouse_input_c(x1, x2, y1, y2):
    global x, y, input_state, eq, a
    if x1 < x < x2 and y1 < y < y2:
        if not input_state:
            input_state = True
            eq = ''
            a = ''
        elif input_state:
            eq = ''


def eval_ans():
    global a, input_state, eq
    try:
        a = eval(eq)
        input_state = False
    except:
        a = 'ERROR'
        input_state = False


# Main loop
while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = pygame.mouse.get_pos()
            mouse_input(20, 196, 482, 560, 1)
            mouse_input(214, 390, 482, 560, 2)
            mouse_input(408, 582, 482, 560, 3)
            mouse_input(20, 196, 390, 468, 4)
            mouse_input(214, 390, 390, 468, 5)
            mouse_input(408, 582, 390, 468, 6)
            mouse_input(20, 196, 296, 375, 7)
            mouse_input(214, 390, 296, 375, 8)
            mouse_input(408, 582, 296, 375, 9)
            mouse_input(20, 252, 576, 656, 0)
            mouse_input(268, 418, 576, 656, '(')
            mouse_input(434, 582, 576, 656, ')')
            mouse_input_oper(600, 778, 482, 560, '+')
            mouse_input_oper(600, 778, 390, 468, '-')
            mouse_input_oper(600, 778, 296, 375, '*')
            mouse_input_oper(600, 778, 202, 284, '/')
            mouse_input_oper(408, 582, 202, 284, '.')
            mouse_input_oper(214, 390, 202, 284, '/100')
            mouse_input_backspace(684, 748, 34, 62)
            mouse_input_c(20, 196, 202, 284)
            if 600 < x < 778 and 576 < y < 656:
                eval_ans()
            if 28 < x < 56 and 148 < y < 172:
                eval_ans()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_KP_ENTER or event.key == pygame.K_EQUALS:
                eval_ans()
            if event.key == pygame.K_BACKSPACE:
                if not input_state:
                    input_state = True
                    eq = ''
                    a = ''
                elif input_state:
                    eq = f'{eq[:-1]}'
            if event.key == pygame.K_a:
                if not input_state:
                    eq = f'{a}'
                    a = ''
                    input_state = True
            if event.key == pygame.K_KP_PLUS or event.key == pygame.K_PLUS:
                input_oper('+')
            if event.key == pygame.K_KP_MINUS or event.key == pygame.K_MINUS:
                input_oper('-')
            if event.key == pygame.K_KP_MULTIPLY or event.key == pygame.K_ASTERISK:
                input_oper('*')
            if event.key == pygame.K_KP_DIVIDE or event.key == pygame.K_SLASH:
                input_oper('/')
            if event.key == pygame.K_0 or event.key == pygame.K_KP0:
                input_num(0)
            if event.key == pygame.K_1 or event.key == pygame.K_KP1:
                input_num(1)
            if event.key == pygame.K_2 or event.key == pygame.K_KP2:
                input_num(2)
            if event.key == pygame.K_3 or event.key == pygame.K_KP3:
                input_num(3)
            if event.key == pygame.K_4 or event.key == pygame.K_KP4:
                input_num(4)
            if event.key == pygame.K_5 or event.key == pygame.K_KP5:
                input_num(5)
            if event.key == pygame.K_6 or event.key == pygame.K_KP6:
                input_num(6)
            if event.key == pygame.K_7 or event.key == pygame.K_KP7:
                input_num(7)
            if event.key == pygame.K_8 or event.key == pygame.K_KP8:
                input_num(8)
            if event.key == pygame.K_9 or event.key == pygame.K_KP9:
                input_num(9)
            if event.key == pygame.K_PERIOD or event.key == pygame.K_KP_PERIOD:
                input_oper('.')
    if len(eq) < 18:
        show_cal(textX, textY)
    elif len(eq) >= 18:
        len_eq = len(eq)
        show_cal((textX - (len_eq - 18) * 39.5), textY)
    show_ans(textX, textY + 100)
    pygame.display.update()
