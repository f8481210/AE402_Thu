import pygame

#顏色設定區 tuple
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)

#視窗設定
pygame.init()
size = (700,500)
screen = pygame.display.set_mode(size)
done = False
clock = pygame.time.Clock()

# -------- 遊戲設定 -----------
#位置

#選擇

#分數

#函式 - 按對了就要換亮新的鍵，而且不能重複亮


# -------- 主要的程式迴圈 -----------
while not done: #遊戲執行中
    # --- 事件迴圈 event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    #設定背景顏色
    
    #按鍵判斷
            
            #按左鍵，且亮左鍵
            
            #按右鍵，且亮右鍵
            
            #按上鍵，且亮上鍵
            
            #按下鍵，且亮下鍵
    
    #畫方塊 - 選到的鍵要是黃色，其餘是黑色
            
    #把分數顯示在視窗欄
    
    #其他設定
    pygame.display.flip()
    clock.tick(5)
    
#遊戲結束
pygame.quit()

