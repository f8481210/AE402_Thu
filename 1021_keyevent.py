import pygame

#顏色設定區 tuple
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)

pygame.init()

#視窗設定
size = (400, 400)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("TEST")

done = False

clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                print('up')
            elif event.key == pygame.K_DOWN:
                print('down')
            elif event.key == pygame.K_LEFT:
                print('left')
            elif event.key == pygame.K_RIGHT:
                print('right')
            

    screen.fill(BLACK)

    # 主要程式碼

    
    pygame.display.flip()

    clock.tick(5)

pygame.quit()

