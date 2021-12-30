import pygame, random, math, time

#顏色設定區 tuple
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
RED      = ( 225,   0,   0)
BLUE     = (   0,   0, 255)
GREEN    = (0,255,0)

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
        self.direction = 360 - self.direction

    def bouncelr(self):  #左右邊界反彈
        self.direction = (180 - self.direction) % 360
            
class Brick(pygame.sprite.Sprite):  #磚塊角色
    def __init__(self, color, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([38, 13]) #38*13
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Pad(pygame.sprite.Sprite):  #滑板角色
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #滑板圖片
        self.image = pygame.image.load("pad.png")
        self.image.convert()
        self.rect = self.image.get_rect()
        self.rect.x = int((screen.get_width() - self.rect.width)/2)  #滑板位置
        self.rect.y = screen.get_height() - self.rect.height - 20
 
    def update(self):  #滑板位置隨滑鼠移動
        pos = pygame.mouse.get_pos() #取得滑鼠坐標
        self.rect.x = pos[0]  #滑鼠x坐標
        if self.rect.x > screen.get_width() - self.rect.width:  #不要移出右邊界
            self.rect.x = screen.get_width() - self.rect.width

def gameover(message):  #結束程式
    global running            
    text = font1.render(message, 1, BLUE)  #顯示訊息
    screen.blit(text, (screen.get_width()/2-100,screen.get_height()/2-20))
    pygame.display.update()  #更新畫面
    time.sleep(3)  #暫停3秒
    running = False  #結束程式

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
score = 0  
#下方訊息字體
font = pygame.font.SysFont("SimHei", 20)  
#結束程式訊息字體
font1 = pygame.font.SysFont("SimHei", 32)
#接到磚塊音效
soundhit = pygame.mixer.Sound("hit.wav")
#接到滑板音效
soundpad = pygame.mixer.Sound("pad.wav")
#建立全部角色群組
allsprite = pygame.sprite.Group()
#建立磚塊角色群組
bricks = pygame.sprite.Group()
#建立紅色球物件
ball = Ball(10, 300, 350, 10, RED)
#加入全部角色群組
allsprite.add(ball)
#建立滑板球物件
pad = Pad()
#加入全部角色群組
allsprite.add(pad)
#3列方塊
for i in range(3):
    #每列15磚塊
    for j in range(15):
        #1,2列為綠色磚塊
        if  i==0 or i==1:
            brick = Brick(GREEN, j * 40 + 1, i * 15 + 1)
        if i==2 or i == 3:
            #3,4列為藍色磚塊
            brick = Brick(BLUE, j * 40 + 1, i * 15 + 1)
        #加入磚塊角色群組
        bricks.add(brick)
        #加入全部角色群組
        allsprite.add(brick)
#起始訊息
msgstr = "按滑鼠左鍵開始遊戲！"
playing = False  #開始時球不會移動
running = True

# -------- 主要的程式迴圈 -----------
while running:
    clock.tick(30)
    # --- 事件迴圈 event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    buttons = pygame.mouse.get_pressed()  #檢查滑鼠按鈕
    if buttons[0]:  #按滑鼠左鍵後球可移動
        playing = True
    if playing == True:  #遊戲進行中
        screen.blit(background, (0,0))  #清除繪圖視窗
        fail = ball.update()  #移動球體
        if fail:  #球出界
            gameover("失敗，再接再勵！")
        pad.update()  #更新滑板位置
        hitbrick = pygame.sprite.spritecollide(ball, bricks, True)  #檢查球和磚塊碰撞
        if len(hitbrick) > 0:  #球和磚塊發生碰撞
            score += len(hitbrick)  #計算分數
            soundhit.play()  #球撞磚塊聲
            ball.rect.y += 20  #球向下移
            ball.bounceup()  #球反彈
            if len(bricks) == 0:  #所有磚塊消失
                gameover("恭喜，挑戰成功！")
        hitpad = pygame.sprite.collide_rect(ball, pad)  #檢查球和滑板碰撞
        if hitpad:  #球和滑板發生碰撞
            soundpad.play()  #球撞滑板聲
            ball.bounceup()  #球反彈
        allsprite.draw(screen)  #繪製所有角色
        msgstr = "得分：" + str(score)
    msg = font.render(msgstr, 1, BLUE)
    screen.blit(msg, (screen.get_width()/2-60,screen.get_height()-20))  
    #其他設定
    pygame.display.update()
#遊戲結束
pygame.quit()