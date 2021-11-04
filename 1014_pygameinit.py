import pygame

#顏色設定區 tuple
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)

#視窗設定
pygame.init()
size = (400, 400)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("遊戲標題")
done = False
clock = pygame.time.Clock()

# -------- 遊戲設定 -----------

# -------- 主要的程式迴圈 -----------
while not done: #遊戲執行中
    # --- 事件迴圈 event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    #主要程式碼
    
    #其他設定
    pygame.display.flip()
    clock.tick(5)
    
#遊戲結束
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
