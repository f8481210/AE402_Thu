import pygame

#顏色設定區 tuple
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)

#視窗設定
pygame.init()
size = (400, 400)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("SHIP")
done = False
clock = pygame.time.Clock()

# -------- 遊戲設定 -----------


#圖片
player_image = pygame.image.load("1104/playerShip1_orange.png").convert() #飛船

#去掉背景顏色
player_image.set_colorkey(BLACK)

# -------- 主要的程式迴圈 -----------
while not done: #遊戲執行中
    # --- 事件迴圈 event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
    #取得滑鼠座標
    pos = pygame.mouse.get_pos()

    # Copy image to screen:
    screen.blit(player_image,(pos[0]-50,pos[1]-50))
    
    #其他設定
    pygame.display.flip()
    clock.tick(5)

#遊戲結束
pygame.quit()

