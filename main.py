import pygame
import random


running = True

def debug(FPS_cap, n_step_printing):
    global steps_taken

    if FPS_cap != 0:
        clock.tick(FPS_cap)

    if n_step_printing == True:
        print(steps_taken)


steps_taken = 0
pi=0

rows, cols = (480, 480)
all_points = [[0 for i in range(cols)] for j in range(rows)]

points_in_circle = 0

n_steps_values = []
n_steps = [10, 100, 1000, 10000, 100000, 1000000]


def blit_all(is_optimised):
    global all_points
    global steps_taken
    global pi

    key = 1

    if is_optimised == True:
        if steps_taken>1000:
            key = random.randint(1, int(steps_taken/20))
        elif steps_taken>500:
            key = random.randint(1,25)
        if steps_taken>250:
            key = random.randint(1,5)
        elif steps_taken>100:
            key = random.randint(1,2)


    if key == 1:
        i=0
        while i<480:
            j=0
            while j<480:
                if all_points[i][j]==1:
                    screen.blit(red_tag, (120+i, 120+j))
                if all_points[i][j]==2:
                    screen.blit(blue_tag, (120+i, 120+j))
                j=j+1
            i=i+1

        pygame.display.update(rect_left)

    blit_n_steps()
    blit_pi(pi)
    pygame.display.update(rect_right)


def new_point():
    global all_points
    global steps_taken
    global points_in_circle


    i=random.randint(0,479)
    j=random.randint(0,479)


    distance = float((i**2 + (479-j)**2)**0.5)

    if distance < float(480):
        points_in_circle = points_in_circle + 1
        all_points[i][j] = 1

    else:
        all_points[i][j] = 2

    steps_taken = steps_taken + 1


def blit_n_steps(): #yes it's sloppy and bad and I don't care lmao
    global n_steps_values
    n_steps_list = []

    if len(n_steps_values) > 0:
        n_10_pi = small_font.render(("n=10;       π=" + str(n_steps_values[0])), False, (0, 0, 0))
        n_steps_list.append(n_10_pi)
    if len(n_steps_values) > 1:
        n_100_pi = small_font.render(("n=100;      π=" + str(n_steps_values[1])), False, (0, 0, 0))
        n_steps_list.append(n_100_pi)
    if len(n_steps_values) > 2:
        n_1000_pi = small_font.render(("n=1000;     π=" + str(n_steps_values[2])), False, (0, 0, 0))
        n_steps_list.append(n_1000_pi)
    if len(n_steps_values) > 3:
        n_10000_pi = small_font.render(("n=10000;    π=" + str(n_steps_values[3])), False, (0, 0, 0))
        n_steps_list.append(n_10000_pi)
    if len(n_steps_values) > 4:
        n_100000_pi = small_font.render(("n=100000;   π=" + str(n_steps_values[4])), False, (0, 0, 0))
        n_steps_list.append(n_100000_pi)
    if len(n_steps_values) > 5:
        n_1000000_pi = small_font.render(("n=1000000;  π=" + str(n_steps_values[5])), False, (0, 0, 0))
        n_steps_list.append(n_1000000_pi)
    if len(n_steps_values) > 6:
        n_10000000_pi = small_font.render(("n=10000000; π=" + str(n_steps_values[6])), False, (0, 0, 0))
        n_steps_list.append(n_10000000_pi)


    i=0
    while i< len(n_steps_list):
        screen.blit(n_steps_list[i], (720, 200+30*i))
        i=i+1


def get_n_steps(pi_value):
    global steps_taken
    global n_steps_values
    global n_steps

    for x in n_steps:
        if steps_taken == x:
            n_steps_values.append(str(pi_value))


def blit_pi(pi_value):

    pi_list = list(str(pi_value))
    if len(pi_list) < 18:
        while len(pi_list) < 18:
            pi_list.append("0")

    str_pi = ("π=" + "".join(pi_list))

    current_pi = main_font.render(str_pi, False, (0, 0, 0))
    screen.blit(current_pi, (720, 124))


if __name__ == '__main__':

    screen = pygame.display.set_mode((1280,720))

    main_graphics = pygame.image.load("main_graphics_2.png").convert_alpha()
    red_tag = pygame.image.load("red_tag3.png").convert_alpha()
    blue_tag = pygame.image.load("blue_tag3.png").convert_alpha()

    pygame.font.init()

    main_font = pygame.font.SysFont('Courier New', 40)
    small_font = pygame.font.SysFont('Courier New', 30)

    rect_left = pygame.Rect((0, 0), (608, 720))
    rect_right = pygame.Rect((608, 0), (672, 720))

    clock = pygame.time.Clock()

    while running:

        screen.fill((128,128,128))
        screen.blit(main_graphics, (124,124))


        blit_all(True)
        new_point()


        pi = float(4*points_in_circle/steps_taken)

        get_n_steps(pi)



        events = pygame.event.get()
        for event in events:
            if event.type == pygame.WINDOWCLOSE:
                running=False


        debug(0, True)
