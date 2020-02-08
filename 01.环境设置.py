import pygame
from pygame.locals import *
import sys
import time

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 720

DEFAULT_FPS = 60
DEFAULT_DELAY = 1.0/DEFAULT_FPS # 0.016666666666666666

if __name__ == '__main__':
    pygame.init()
    window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))

    font = pygame.font.Font('font/happy.ttf',44)
    text = font.render('de', True, (255, 0, 0))
    window.blit(text, (10, 10))

    # 玩家车辆
    car = pygame.image.load('img/car.png')
    x = 300
    y = 400

    # 画三条竖线
    points1 = [(10, 0), (10, WINDOW_HEIGHT)]
    points2 = [(WINDOW_WIDTH/2, 0), (WINDOW_WIDTH/2, WINDOW_HEIGHT)]
    points3 = [(WINDOW_WIDTH-10, 0), (WINDOW_WIDTH-10, WINDOW_HEIGHT)]



    while True:
        # 填充背景
        window.fill((0,0,0))
        # 渲染竖线
        pygame.draw.lines(window, (0, 255, 0), 0, points1, 1)
        pygame.draw.lines(window, (0, 255, 0), 0, points2, 1)
        pygame.draw.lines(window, (0, 255, 0), 0, points3, 1)

        # 显示车辆
        window.blit(car, (x, y))
        # 渲染
        pygame.display.flip()
        events = pygame.event.get()
        for e in events:
            if e.type == QUIT:
                pygame.quit()
                sys.exit(0)
            if e.type == KEYDOWN:
                if e.key == K_LEFT:
                    print('left')
                    x -= 100
                if e.key == K_RIGHT:
                    print('right')
                    x += 100

