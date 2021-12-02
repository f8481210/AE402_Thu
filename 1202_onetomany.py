#1對50
#檔名：1202_onetomany
import pygame,random

# 顏色常數
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)

#Block類別: 繼承自Sprite類別
class Block(pygame.sprite.Sprite):
    #初始化
    def __init__(self, color, width, height):
        #呼叫父類別
        super().__init__()
        #創造一個block的image
        self.image = pygame.Surface([width, height])
        #填入顏色到image
        self.image.fill(color)
        #抓出image的rect物件，設定給block的屬性rect
        self.rect = self.image.get_rect()
        
        
#初始化pygame
pygame.init()
#設定設窗大小
screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])

#建立一個所有角色的group(player,blocks)
all_sprites_list = pygame.sprite.Group()

#建立只有block的group
block_list = pygame.sprite.Group()

for i in range(50):
    #產生一個黑方塊
    block = Block(BLACK, 20, 15)
    #產生方塊座標
    block.rect.x = random.randrange(screen_width)
    block.rect.y = random.randrange(screen_height)
    #將block加到兩個角色群組中
    block_list.add(block)
    all_sprites_list.add(block)

#紅色player
player = Block(RED, 20, 15)
all_sprites_list.add(player)

#分數
score = 0
font = pygame.font.Font(None, 50)

#遊戲設定
done = False
clock = pygame.time.Clock()
start_ticks=pygame.time.get_ticks()

#主要程式碼
while not done:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            play = False 
            

    #背景
    screen.fill(WHITE)
    
    # 計算秒數
    seconds=int((pygame.time.get_ticks()-start_ticks)/1000) 
    
    #取得滑鼠位置
    pos = pygame.mouse.get_pos()
    player.rect.x = pos[0]
    player.rect.y = pos[1]
    
    #判斷player和block是否碰撞
    blocks_hit_list = pygame.sprite.spritecollide(player,block_list,True)
    
    for i in blocks_hit_list:
        score += 1
    
    #畫出所有角色
    all_sprites_list.draw(screen)
    
    # 顯示分數
    message = str(score)+' point'
    text = font.render(message, 10, BLACK)
    screen.blit(text, (10,10))
    
    #顯示時間
    t = font.render(str(seconds), 10, RED)
    screen.blit(t, (10,40))
    
    if seconds>10:
        text = font.render("GAME OVER", 50, BLACK)
        screen.blit(text, (100,100))
        done = True
        
    #遊戲更新
    pygame.display.flip()
    clock.tick(60)
    
pygame.quit()
