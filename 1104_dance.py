import pygame,random

#顏色設定區 tuple
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
YELLOW   = ( 255, 255,   0)

#視窗設定
pygame.init()
size = (700,500)
screen = pygame.display.set_mode(size)
done = False
clock = pygame.time.Clock()

# -------- 遊戲設定 -----------
#位置 右  下   左  上
x = [300,250,200,250]
y = [250,250,250,200]
#選擇 - 儲存亮的方塊位置
choice = 0 # 右 = 0 ,下 = 1 , 左 = 2 , 上 = 3
#分數
score = 0
#函式 - 按對了就要換亮新的鍵，而且不能重複亮
def new_color(choice):
    temp = random.randint(0,3)
    while choice == temp:
        temp = random.randint(0,3)
    choice = temp
    return choice 

# -------- 主要的程式迴圈 -----------
while not done: #遊戲執行中
    # --- 事件迴圈 event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    #設定背景顏色
    screen.fill(WHITE)
    #按鍵判斷
    if event.type == pygame.KEYDOWN:       
            #按左鍵，且亮左鍵
            if event.key == pygame.K_LEFT and choice == 2:
                choice = new_color(choice)
                score+=1
            #按右鍵，且亮右鍵
            if event.key == pygame.K_RIGHT and choice == 0:
                choice = new_color(choice)   
                score+=1
            #按上鍵，且亮上鍵           
            if event.key == pygame.K_UP and choice == 3:
                choice = new_color(choice)
                score+=1
            #按下鍵，且亮下鍵
            if event.key == pygame.K_DOWN and choice == 1:
                choice = new_color(choice)
                score+=1
    #畫方塊 - 選到的鍵要是黃色，其餘是黑色
    for i in range(4):
        if choice == i:
            color = YELLOW
        else:
            color = BLACK
        pygame.draw.rect(screen, color, [x[i],y[i], 40, 40])
            
    #把分數顯示在視窗欄
    pygame.display.set_caption(str(score))
    
    #遊戲結束條件
    if score == 10 :
        break
    #其他設定
    pygame.display.flip()
    clock.tick(5)
    
#遊戲結束
pygame.quit()

