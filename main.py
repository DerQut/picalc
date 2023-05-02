import pygame
import time
import random


running = True

steps_to_take = 10000000
steps_taken = 0

rows, cols = (480, 480)
all_points = [[0 for i in range(cols)] for j in range(rows)]

points_in_circle = 0

frame = 0


def blit_all():
    global all_points

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

def new_point():
    global all_points
    global steps_taken
    global points_in_circle


    i=random.randint(0,479)
    j=random.randint(0,479)

    x=i
    y=479-j

    distance = float((x**2 + y**2)**0.5)

    if distance < float(480):
        points_in_circle = points_in_circle + 1
        all_points[i][j] = 1

    else:
        all_points[i][j] = 2

    steps_taken = steps_taken + 1
    print(steps_taken)


if __name__ == '__main__':

    screen = pygame.display.set_mode((1280,720))

    main_graphics = pygame.image.load("main_graphics_2.png").convert_alpha()
    red_tag = pygame.image.load("red_tag3.png").convert_alpha()
    blue_tag = pygame.image.load("blue_tag3.png").convert_alpha()

    pygame.font.init()
    my_font = pygame.font.SysFont('Comic Sans MS', 30)

    while running:

        screen.fill((128,128,128))
        screen.blit(main_graphics, (124,124))


        blit_all()

        frame = frame+1
        if frame == 1:
            new_point()
            frame = 0

        pi = float(4*points_in_circle/steps_taken)

        str_pi = ("π="+str(pi))

        text_surface = my_font.render(str_pi, False, (0, 0, 0))
        screen.blit(text_surface, (0, 0))

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.WINDOWCLOSE:
                running=False

        pygame.display.update()