import pygame

#顏色設定區 tuple
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)

pygame.init()

#視窗設定
size = (400, 400)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("PIC")

done = False

clock = pygame.time.Clock()

# -------- 主要的程式迴圈 -----------
player_image = pygame.image.load("1028_playerShip1_orange.png").convert() #飛船
#去掉背景顏色
player_image.set_colorkey(BLACK)

while not done: #遊戲執行中
    # --- 事件迴圈 event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    #滑鼠移動
    pos = pygame.mouse.get_pos()
    
        
    screen.fill(WHITE)

    # 主要程式碼
    screen.blit(player_image,(pos[0]-50,pos[1]-50))
    
    pygame.display.flip()

    clock.tick(5)

pygame.quit()

