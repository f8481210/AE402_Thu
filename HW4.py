import pygame

WHITE = (255,255,255)
RED = (255,0,0)
ORANGE = (242,133,0)
YELLOW = (255,255,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
PURPLE = (255,0,255)

SKY = (135, 206,235)



pygame.init()
done = False
size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("彩虹")
clock = pygame.time.Clock()

while not done:

    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True 

    screen.fill(SKY)

    #pygame.draw.arc(畫布, 顏色, [x坐標, y坐標, x直徑, y直徑], 起始角, 結束角, 線寬)
    pygame.draw.arc(screen, RED, [100,200,300,300],0,3,10)
    pygame.draw.arc(screen, ORANGE, [90,190,320,320],0,3,10)
    pygame.draw.arc(screen, YELLOW, [80,180,340,340],0,3,10)
    pygame.draw.arc(screen, GREEN, [70,170,360,360],0,3,10)
    pygame.draw.arc(screen, BLUE, [60,160,380,380],0,3,10)
    pygame.draw.arc(screen, PURPLE, [50,150,400,400],0,3,10)

    pygame.draw.circle(screen,YELLOW,[500,100],60)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()

    


