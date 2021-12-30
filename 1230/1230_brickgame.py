import pygame, random, math, time

#顏色設定區 tuple
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
RED      = ( 225,   0,   0)
BLUE     = (   0,   0, 255)

class Ball(pygame.sprite.Sprite):  #球體角色
    dx = 0  #x位移量
    dy = 0  #y位移量
    x = 0  #球x坐標
    y = 0  #球y坐標
    direction = 0  #球移動方向
    speed = 0  #球移動速度
 
    def __init__(self, speed, srx, sry, radium, color):
        pygame.sprite.Sprite.__init__(self)
        self.speed = speed
        self.x = srx
        self.y = sry
        self.image = pygame.Surface([radium*2, radium*2])  #繪製球體
        self.image.fill(WHITE)
        pygame.draw.circle(self.image, color, (radium,radium), radium, 0)
        self.rect = self.image.get_rect()  #取得球體區域
        self.rect.center = (srx,sry)  #初始位置
        self.direction = random.randint(40,70)  #移動角度
 
    def update(self):  #球體移動
        radian = math.radians(self.direction)  #角度轉為弳度
        self.dx = self.speed * math.cos(radian)  #球水平運動速度
        self.dy = -self.speed * math.sin(radian)  #球垂直運動速度
        self.x += self.dx  #計算球新坐標
        self.y += self.dy
        self.rect.x = self.x  #移動球圖形
        self.rect.y = self.y
        if(self.rect.left <= 0 or self.rect.right >= screen.get_width()-10):  #到達左右邊界
            self.bouncelr()
        elif(self.rect.top <= 10):  #到達上邊界
            self.rect.top = 10
            self.bounceup()
        if(self.rect.bottom >= screen.get_height()-10):  #到達下邊界出界
            return True
        else:
            return False
 
    def bounceup(self):  #上邊界反彈
        

    def bouncelr(self):  #左右邊界反彈
        
            
class Brick(pygame.sprite.Sprite):  #磚塊角色
    def __init__(self, color, x, y):
        pygame.sprite.Sprite.__init__(self)


class Pad(pygame.sprite.Sprite):  #滑板角色
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

 
    def update(self):  #滑板位置隨滑鼠移動


def gameover(message):  #結束程式

# -------- 遊戲設定 -----------
#視窗設定
pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("打磚塊遊戲")
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill(WHITE)
clock = pygame.time.Clock()
#得分
#下方訊息字體
#結束程式訊息字體
#接到磚塊音效
#接到滑板音效
#建立全部角色群組
#建立磚塊角色群組
#建立紅色球物件
 #加入全部角色群組
#建立滑板球物件
#加入全部角色群組

#3列方塊
#每列15磚塊
#1,2列為綠色磚塊

#3,4列為藍色磚塊

#加入磚塊角色群組
#加入全部角色群組
#起始訊息
playing = False  #開始時球不會移動
running = True

# -------- 主要的程式迴圈 -----------
while running:
    clock.tick(30)
    # --- 事件迴圈 event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #檢查滑鼠按鈕
    #按滑鼠左鍵後球可移動
            
    #主要程式碼
    #遊戲進行中
    #清除繪圖視窗
    #移動球體
    #球出界
    
    #更新滑板位置
    #檢查球和磚塊碰撞
    #球和磚塊發生碰撞
    #計算分數
    #球撞磚塊聲
    #球向下移
    #球反彈
    #所有磚塊消失
    
    #檢查球和滑板碰撞
    #球和滑板發生碰撞
    #球撞滑板聲
    #球反彈
    #繪製所有角色
    
    #繪製訊息
            
    #其他設定
    pygame.display.update()
#遊戲結束
pygame.quit()