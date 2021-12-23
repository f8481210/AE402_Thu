import pygame,random,math

#顏色設定區 tuple
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
RED      = ( 225,   0,   0)
BLUE     = (   0,   0, 255)

#視窗設定
pygame.init()
size = (400, 400)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("建立及使用角色")
done = False
clock = pygame.time.Clock()

#類別設定 繼承Sprite
class ball(pygame.sprite.Sprite):
    #座標
    x = 0
    y = 0
    #dx dy 移動的位移
    dx = 0
    dy = 0
    def __init__(self,speed,color,bx,by,radium):
        pygame.sprite.Sprite.__init__(self)
        self.x = bx
        self.y = by
        
        #繪製球體 長寬=直徑
        self.image = pygame.Surface([radium*2, radium*2])
        self.image.fill(WHITE)
        
        pygame.draw.circle(self.image, color, (radium,radium), radium, 0)
        #取得球體區域
        self.rect = self.image.get_rect()
        #初始位置
        self.rect.center = (self.x,self.y)
        
        #隨機取得球移動角度
        #為什麼設定不是0~90度
        direction = random.randint(20,70)
        #角度轉為弳度
        radian = math.radians(direction)
        # x軸 水平移動公式： 速度*cos(勁度)
        self.dx = speed * math.cos(radian)
        # y軸 垂直移動公式： 速度*sin(勁度)
        self.dy = -speed * math.sin(radian)
        
    def update(self):
        #計算球的新座標
        self.x += self.dx
        self.y += self.dy
        #移動球
        self.rect.x = self.x
        self.rect.y = self.y
        
        #判斷有沒有碰到左右邊界 X軸變號
        if(self.rect.left <= 0 or self.rect.right >= screen.get_width()):
            self.dx *= -1  #水平速度變號
        #判斷有沒有碰到上下邊界
        elif (self.rect.top <= 5 or self.rect.bottom >= screen.get_height()-5):
            self.dy *= -1  #垂直速度變號
    
    def collidebounce(self):
        self.dx *= -1

# -------- 遊戲設定 -----------
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill(WHITE)

#建立角色群組
allsprite = pygame.sprite.Group()
redball = ball(8, RED, 100, 100, 10)
allsprite.add(redball)
blueball = ball(13, BLUE, 250, 200, 15)
allsprite.add(blueball)

# -------- 主要的程式迴圈 -----------
while not done: #遊戲執行中
    # --- 事件迴圈 event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    #主要程式碼
    screen.blit(background, (0,0))  #清除繪圖視窗
    redball.update()  #物件更新
    blueball.update()
    allsprite.draw(screen)
    result = pygame.sprite.collide_rect(redball, blueball)
    if result == True:
        redball.collidebounce()
        blueball.collidebounce()
    
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