# -*- coding: utf-8 -*-
import pygame , random
from queue import Queue

# 顏色設定區 tuple
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
RED = (255, 0, 0)

# 貪吃蛇初始設定
# 寬與高(正方形)
segment_width = 48
segment_height = 48
# 節之間的間隙
segment_margin = 2
# 蛇頭的初始座標
segment_head_x = 0
segment_head_y = 0

# 設定初始速度(初始往右移動)
x_change = 1
y_change = 0

# Segment類別
class Segment(pygame.sprite.Sprite):
    """ Class to represent one segment of the snake. """
    # -- 方法
    # 建構式
    def __init__(self, x, y):
        # 呼叫父建構式
        super().__init__()

        # 設定寬與高
        self.image = pygame.Surface([segment_width, segment_height])
        self.image.fill(WHITE)

        # 左上角座標
        self.rect = self.image.get_rect()
        self.rect.x = x*(segment_width+segment_margin)
        self.rect.y = y*(segment_height+segment_margin)
        
        self.x = x
        self.y = y
# 初始化pygame
pygame.init()
# 視窗設定
size = (800,600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("snake")
done = False
clock = pygame.time.Clock()

# -------- 遊戲設定 -----------

eat = True
score = 0

# 所有角色的group物件
allspriteslist = pygame.sprite.Group()

# 創造初始的貪食蛇(from queue import Queue)
snake_segments = Queue()

#創造初始的貪食蛇(一開始要畫幾節的蛇)
for i in range(5):
    x = 3+i
    y = 3
    segment = Segment(x, y)
    # 放入QUEUE裡和GROUP裡
    snake_segments.put(segment)
    allspriteslist.add(segment)
    segment_head_x = x
    segment_head_y = y

# -------- 主要的程式迴圈 -----------
while not done: # 遊戲執行中
    # --- 事件迴圈 event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT: # 右
                x_change = 1
                y_change = 0
            if event.key == pygame.K_LEFT: # 左
                x_change = -1
                y_change = 0
            if event.key == pygame.K_UP: # 上
                x_change = 0
                y_change = -1
            if event.key == pygame.K_DOWN: # 下
                x_change = 0
                y_change = 1
    
    # 背景顏色
    screen.fill(BLACK)
    
    # 創造最新的一個segment(新的頭)
    segment_head_x = segment_head_x + x_change
    segment_head_y = segment_head_y + y_change
    segment = Segment(segment_head_x, segment_head_y)
    
    # 將新的segment插入list中的第一位
    snake_segments.put(segment)
    allspriteslist.add(segment)
    
    # apple
    if eat :
        ax = random.randrange(16)
        ay = random.randrange(12)
        eat = False
    else: #還沒吃到蘋果但蛇在移動
        # 拿掉貪食蛇的最後一個segment
        # 利用list的pop()
        old_segment = snake_segments.get()
        allspriteslist.remove(old_segment)
    #產生蘋果
    apple = Segment(ax,ay)
    
    # 判斷又沒有吃到蘋果
    if segment.x == apple.x and segment.y == apple.y:
        score += 1
        eat = True
        pygame.display.set_caption("snake|score: "+ str(score))

    # 畫出GROUP裡所有內容
    pygame.draw.rect(screen,RED,(ax*(segment_width+segment_margin),\
                     ay*(segment_width+segment_margin),\
                     segment_width,segment_height))
    allspriteslist.draw(screen)
    
    # 其他設定
    pygame.display.flip()
    clock.tick(5)
    
# 遊戲結束
pygame.quit()