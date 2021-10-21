import pygame

#顏色設定區 tuple
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)

pygame.init()

#視窗設定
size = (400, 400)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("下雪動畫")



done = False

clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(BLACK)

    #主要程式


 
    pygame.display.flip()

    clock.tick(5)

pygame.quit()

# 1.產生一個串列snow_list
# 2.再隨機產生一個串列[x,y]，append進snow_list
# 3.snow_list = [ [x1,y2] , [x2,y2] , ... , [x50,y50] ]