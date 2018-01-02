import sys
import pygame

def run():

    pygame.init()
    screen = pygame.display.set_mode((750,1000))
    pygame.display.set_caption("测试按键")


    ba_color = (60,60,60,0)

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT \
                    or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                print(event)
                print(event.key)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print(event)
                print(event.button)
                #print(event.mousebutton)

        screen.fill(ba_color)

        pygame.display.flip()

run()