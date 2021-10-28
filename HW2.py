import pygame,random

#顏色設定區 tuple
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)

pygame.init()

#視窗設定
size = (400, 400)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("BOX")

done = False

clock = pygame.time.Clock()

# -------- 主要的程式迴圈 -----------
# 方塊初始位置
x = 0 #左右
y = 0 #上下

while not done:
    # --- 事件迴圈 event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            
            
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                y = y-10
            elif keys[pygame.K_DOWN]:
                y = y+10
            elif keys[pygame.K_LEFT]:
                x = x-10
            elif keys[pygame.K_RIGHT]:
                x = x+10
            elif event.key == pygame.K_SPACE:
                x = random.randrange(0,400)
                y = random.randrange(0,400)
            
            
        

    screen.fill(BLACK)

    # 主要程式碼
    pygame.draw.rect(screen, WHITE, [x + 10, y + 10, 10, 10])
    
    pygame.display.flip()

    clock.tick(5)

pygame.quit()

