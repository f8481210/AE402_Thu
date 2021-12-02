#檔名：1125_OneToTen
#碰撞遊戲 一對十

#匯入模組
import pygame , random, time

#設定顏色
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)

#遊戲初始化
pygame.init()

#設定視窗
screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])

#設定方塊_大小
player_w = 50
player_h = 50
block_w = 50
block_h =50

block_x = []
block_y = []
collision = []

#設定方塊_初始位置
player_x = 0
player_y = 0

for i in range(10):
    block_x.append(random.randrange(screen_width))
    block_y.append(random.randrange(screen_height))
    #判斷有無撞到的布林變數
    collision.append(False)

#分數
score = 0

#font物件
font = pygame.font.Font(None, 50)

#遊戲設定
done = False
clock = pygame.time.Clock()

#遊戲初始時間
start = pygame.time.get_ticks()

#遊戲主要程式
while not done:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            done = True
    
    #取得時間
    second = int((pygame.time.get_ticks()-start)/1000)
    
    
    #判斷是否碰撞到了
    for i in range(10):
        
        xin = block_x[i]<=player_x<=block_x[i]+block_w  or \
                block_x[i]<=player_x+player_w<=block_x[i]+block_w
        yin = block_y[i]<=player_y<=block_y[i]+block_h or \
                block_y[i]<=player_y+player_h<=block_y[i]+block_h
    
        if xin and yin and not collision[i]:
            collision[i] = True
            score += 1

    #背景顏色
    screen.fill(WHITE)
    
    #取得滑鼠座標 pos[x,y]
    pos = pygame.mouse.get_pos()
    player_x = pos[0]
    player_y = pos[1]
    pygame.draw.rect(screen, RED, [player_x, player_y, player_w, player_h])
    
    for i in range(10):
        if not collision[i]:
            pygame.draw.rect(screen, BLACK, [block_x[i], block_y[i], block_w, block_h])
    
    #顯示分數
    message = str(score)+' point'
    text = font.render(message,True, BLACK)
    screen.blit(text, (10,10))
    
    #顯示時間
    t = font.render(str(second), 10, RED)
    screen.blit(t, (40,40))
    
    if score == 10:
        text = font.render("gameover",50,BLACK)
        screen.blit(text, (100,100))
        done = True
        
    
    #新畫面更新
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
    
'''
作業：完成碰撞遊戲 - 形成10個隨機位置的黑色方塊，使玩家可以碰撞，
若10秒內沒有完成遊戲，則顯示gameover字樣並遊戲結束。
若有在10秒內碰撞完，顯示gamefinish字樣並遊戲結束。
'''







