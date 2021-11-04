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
#背景
background_image = pygame.image.load("saturn_family1.jpg").convert()
#背景圖片的座標
background_position = [0, 0]
#圖片
player_image = pygame.image.load("playerShip1_orange.png").convert() #飛船
#去掉背景顏色
player_image.set_colorkey(BLACK)

#背景音樂BGM
pygame.mixer.music.load("MIT_Concert_Choir_O_Fortuna.ogg")
pygame.mixer.music.play()
#音效
click = pygame.mixer.Sound("laser5.ogg")

# -------- 主要的程式迴圈 -----------
while not done: #遊戲執行中
    # --- 事件迴圈 event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        #判斷滑鼠是否按下去
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click.play()
            
    #取得滑鼠座標
    pos = pygame.mouse.get_pos()

    # Copy image to screen:
    screen.blit(background_image,background_position)
    screen.blit(player_image,(pos[0]-50,pos[1]-50))
    
    #其他設定
    pygame.display.flip()
    clock.tick(5)

#遊戲結束
pygame.quit()

