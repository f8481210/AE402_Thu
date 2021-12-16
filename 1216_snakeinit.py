# -*- coding: utf-8 -*-
import pygame
from queue import Queue

# 顏色設定區 tuple
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)

# 貪吃蛇初始設定
# 寬與高(正方形)
segment_width = 
segment_height = 
# 節之間的間隙
segment_margin = 
# 蛇頭的初始座標
segment_head_x = 0
segment_head_y = 0

# 設定初始速度(初始往右移動)
x_change = 
y_change = 



# Segment類別
class Segment(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        
        # 設定寬與高
        self.image = pygame.Surface([segment_width, segment_height])
        self.image.fill(WHITE)
        
        # 取得每一節座標 
        self.rect = self.image.get_rect()


        self.x = x
        self.y = y
# 初始化pygame
pygame.init()
# 視窗設定
size = (800,600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("貪吃蛇")
done = False
clock = pygame.time.Clock()

# -------- 遊戲設定 -----------

# 所有角色的group物件
allspriteslist = pygame.sprite.Group()

# 創造初始的貪食蛇(from queue import Queue)
snake_segments = Queue()

#創造初始的貪食蛇(一開始要畫幾節的蛇)
for i in range():
    x =
    y =
    segment = Segment(x, y)
    # 放入QUEUE裡和GROUP裡


# -------- 主要的程式迴圈 -----------
while not done: # 遊戲執行中
    # --- 事件迴圈 event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT: # 右
                x_change = 
                y_change = 0
            if event.key == pygame.K_LEFT: # 左
                x_change =
                y_change = 0
            if event.key == pygame.K_UP: # 上
                x_change = 0
                y_change =
            if event.key == pygame.K_DOWN: # 下
                x_change = 0
                y_change = 
    
    # 背景顏色
    screen.fill(BLACK)
    
    # 創造最新的一個segment(新的頭)
    segment_head_x = segment_head_x + x_change
    segment_head_y = segment_head_y + y_change
    segment = Segment(segment_head_x, segment_head_y)
    
    # 將新的segment插入list中的第一位
    snake_segments.put(segment)
    allspriteslist.add(segment)
    
    
    
    
    
    
    
    # 畫出GROUP裡所有內容
    allspriteslist.draw(screen)
    
    # 其他設定
    pygame.display.flip()
    clock.tick(5)
    
# 遊戲結束
pygame.quit()
