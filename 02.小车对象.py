import pygame
from pygame.locals import *
import sys
import time

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 720

DEFAULT_FPS = 60
DEFAULT_DELAY = 1.0/DEFAULT_FPS -0.002

# 边缘线距离
DEFAULT_OFFICE = 10

# 小车对象
class Car:
    def __init__(self,window):
        self.window = window
        self.img = pygame.image.load('img/car.png')
        self.width = self.img.get_width()
        self.height = self.img.get_height()
        # self.x = (WINDOW_WIDTH/2-self.width)/2+DEFAULT_OFFICE/2
        self.x = (WINDOW_WIDTH/2-self.width)/2+DEFAULT_OFFICE/2+(WINDOW_WIDTH-DEFAULT_OFFICE*2)/2
        self.y = 400
    def display(self):
        self.window.blit(self.img,(self.x,self.y))
    def move_left(self):
        self.x -= (WINDOW_WIDTH - DEFAULT_OFFICE * 2) / 2
        if self.x <0:
            self.x = (WINDOW_WIDTH/2-self.width)/2+DEFAULT_OFFICE/2

    def move_right(self):
        self.x += (WINDOW_WIDTH - DEFAULT_OFFICE * 2) / 2
        if self.x > WINDOW_WIDTH:
            self.x = (WINDOW_WIDTH/2-self.width)/2+DEFAULT_OFFICE/2+(WINDOW_WIDTH-DEFAULT_OFFICE*2)/2



if __name__ == '__main__':
    pygame.init()
    window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))

    font = pygame.font.Font('font/happy.ttf',24)

    # 玩家车辆
    # car = pygame.image.load('img/car.png')
    # x = 300
    # y = 400
    car = Car(window)

    # 画三条竖线
    points1 = [(DEFAULT_OFFICE, 0), (DEFAULT_OFFICE, WINDOW_HEIGHT)]
    points2 = [(WINDOW_WIDTH/2, 0), (WINDOW_WIDTH/2, WINDOW_HEIGHT)]
    points3 = [(WINDOW_WIDTH-DEFAULT_OFFICE, 0), (WINDOW_WIDTH-DEFAULT_OFFICE, WINDOW_HEIGHT)]

    fps = 0


    while True:

        start = time.time()

        window.fill((0,0,0))

        # 渲染fps
        text = font.render('FPS:%d' % fps, True, (255, 255, 0))
        window.blit(text, (300, 10))
        # 填充背景
        # 渲染竖线
        pygame.draw.lines(window, (0, 255, 0), 0, points1, 1)
        pygame.draw.lines(window, (0, 255, 0), 0, points2, 1)
        pygame.draw.lines(window, (0, 255, 0), 0, points3, 1)

        # 显示车辆
        # window.blit(car, (x, y))
        car.display()
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
                    car.move_left()
                if e.key == K_RIGHT:
                    print('right')
                    car.move_right()

        end = time.time()
        cost = end - start
        if cost<DEFAULT_DELAY:
            sleep = DEFAULT_DELAY - cost
        else:
            sleep = 0
        time.sleep(sleep)
        end = time.time()
        fps = 1.0/(end-start)
        print(fps)
