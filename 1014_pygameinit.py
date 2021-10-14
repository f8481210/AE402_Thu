import pygame

#顏色設定區 tuple
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)

#遊戲初始化
pygame.init()

#視窗設定
size = (400, 400)
screen = pygame.display.set_mode(size) #創建視窗
pygame.display.set_caption("123456") #標題

#視窗關閉開關
done = False #未完成

clock = pygame.time.Clock() #FPS禎數

while not done: #無窮迴圈
    #有沒有關掉視窗
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    #背景顏色
    screen.fill(BLACK)

    #主要程式碼
    pygame.draw.circle(screen,RED,(50,50),10,10)

    
    pygame.display.flip() #更新畫面

    clock.tick(5) #每秒鐘執行幾次

pygame.quit()

'''
#矩形
pygame.draw.rect(畫布, 顏色, [x坐標, y坐標, 寬度, 高度], 線寬) 

#圓形
pygame.draw.circle(畫布, 顏色, (x坐標, y坐標), 半徑, 線寬)

#橢圓形 
pygame.draw.ellipse(畫布, 顏色, [x坐標, y坐標, x直徑, y直徑], 線寬)

#圓弧形 
pygame.draw.arc(畫布, 顏色, [x坐標, y坐標, x直徑, y直徑], 起始角, 結束角, 線寬) 

#直線
pygame.draw.line(畫布, 顏色, (x坐標1, y坐標1), (x坐標2, y坐標2), 線寬)
'''
