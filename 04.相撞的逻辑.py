import pygame
from pygame.locals import *
import sys
import time
import random

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 720

DEFAULT_FPS = 60
DEFAULT_DELAY = 1.0/DEFAULT_FPS -0.002

# 边缘线距离
DEFAULT_OFFICE = 10

# 障碍物对象
class Stone:
    def __init__(self,window):
        self.window = window
        self.reset()

    def display(self):
        self.window.blit(self.img,(self.x,self.y))
    def move(self):
        self.y += 5
        if self.y>WINDOW_HEIGHT:
            global score
            score += 10
            self.reset()

    def reset(self):
        self.img = pygame.image.load('img/stone.png')
        self.width = self.img.get_width()
        self.height = self.img.get_height()
        one = (WINDOW_WIDTH / 2 - self.width) / 2 + DEFAULT_OFFICE / 2
        two = (WINDOW_WIDTH/2-self.width)/2+DEFAULT_OFFICE/2+(WINDOW_WIDTH-DEFAULT_OFFICE*2)/2
        self.x = random.choice([one,two])
        self.y = -self.height

# 小车对象
class Car:
    def __init__(self,window):
        self.window = window
        self.img = pygame.image.load('img/car.png')
        self.width = self.img.get_width()
        self.height = self.img.get_height()
        # self.x = (WINDOW_WIDTH/2-self.width)/2+DEFAULT_OFFICE/2
        self.x = (WINDOW_WIDTH/2-self.width)/2+DEFAULT_OFFICE/2+(WINDOW_WIDTH-DEFAULT_OFFICE*2)/2
        self.y = WINDOW_HEIGHT-self.height*2
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

    # 背景音乐
    pygame.mixer_music.load('snd/bg2.ogg')
    pygame.mixer_music.play(-1)

    font = pygame.font.Font('font/happy.ttf',24)
    # 渲染游戏结束
    is_over = False
    font_finish = pygame.font.Font('font/happy.ttf',48)
    text_finish = font_finish.render('游戏结束', True, (255, 0, 0))
    finish_width = text_finish.get_width()
    finish_height = text_finish.get_height()
    finish_x = (WINDOW_WIDTH-finish_width)/2
    finish_y = (WINDOW_HEIGHT-finish_height)/2

    # 玩家车辆
    # car = pygame.image.load('img/car.png')
    # x = 300
    # y = 400
    car = Car(window)
    # 障碍物
    stones = []
    stones.append(Stone(window))

    # 画三条竖线
    points1 = [(DEFAULT_OFFICE, 0), (DEFAULT_OFFICE, WINDOW_HEIGHT)]
    points2 = [(WINDOW_WIDTH/2, 0), (WINDOW_WIDTH/2, WINDOW_HEIGHT)]
    points3 = [(WINDOW_WIDTH-DEFAULT_OFFICE, 0), (WINDOW_WIDTH-DEFAULT_OFFICE, WINDOW_HEIGHT)]

    fps = 0
    score = 0

    while True:

        start = time.time()
        # 填充背景,放在首行
        window.fill((0,0,0))

        # 渲染fps
        text = font.render('FPS:%d' % fps, True, (255, 255, 0))
        window.blit(text, (300, 10))
        # 渲染积分
        text = font.render('积分:%d' % score, True, (255, 255, 0))
        window.blit(text, (10, 10))

        # 渲染竖线
        pygame.draw.lines(window, (0, 255, 0), 0, points1, 1)
        pygame.draw.lines(window, (0, 255, 0), 0, points2, 1)
        pygame.draw.lines(window, (0, 255, 0), 0, points3, 1)

        if is_over:
            window.blit(text_finish, (finish_x, finish_y))

        # 游戏没结束才会显示小车和石头
        if not is_over:
            # 显示小车
            # window.blit(car, (x, y))
            car.display()

            # 相撞的逻辑
            car_rect = pygame.Rect(car.x, car.y, car.width, car.height)
            #显示障碍物
            for stone in stones:
                stone.display()
                stone.move()
                stone_rect = pygame.Rect(stone.x,stone.y,stone.width,stone.height)
                colliderect = pygame.Rect.colliderect(stone_rect, car_rect)
                if colliderect:
                    print('game over-----------------')
                    is_over = True


        # 渲染
        pygame.display.flip()
        events = pygame.event.get()
        for e in events:
            if e.type == QUIT:
                pygame.quit()
                sys.exit(0)
            if e.type == KEYDOWN:
                if e.key == K_LEFT:
                    car.move_left()
                if e.key == K_RIGHT:
                    car.move_right()
                if e.key == K_p:
                    pygame.mixer_music.play(-1)
                if e.key == K_l:
                    pygame.mixer_music.stop()
                if e.key == K_RETURN and is_over:
                    is_over = False
                    stone.reset()
                    score = 0


        end = time.time()
        cost = end - start
        if cost<DEFAULT_DELAY:
            sleep = DEFAULT_DELAY - cost
        else:
            sleep = 0
        time.sleep(sleep)
        end = time.time()
        fps = 1.0/(end-start)
        # print(fps)
