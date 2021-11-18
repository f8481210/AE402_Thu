#檔名：1118_block 創建50個隨機黑色方塊
import pygame , random

# 顏色常數
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)

"""
    Block類別: 繼承自Sprite類別
"""
class Block (pygame.sprite.Sprite):
    #傳入的參數為顏色，還有block的長寬
    def __init__(self,color,width,height):
        #創造一個有特定顏色和大小的image
        super().__init__() #呼叫父類別(Sprite類別)
        
        # 創造一個block的image，接著填入顏色到此image
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        
        # 抓出image的rect物件，設定給block的屬性rect
        self.rect = self.image.get_rect()
    
#遊戲初始化
pygame.init()

#視窗設定 screen
screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])
    
#建立一個角色群組(Group)
block_list = pygame.sprite.Group()

#創建50個黑方塊
for i in range(50):
    #產生block物件
    block = Block(BLACK,20,15)
    #產生隨機座標
    block.rect.x = random.randrange(screen_width)
    block.rect.y = random.randrange(screen_height)
    #加入群組
    block_list.add(block)
    
#遊戲設定
play = True
# 畫面更新頻率
clock = pygame.time.Clock()

# ------- Main ------- #
while play:
    #判斷遊戲是否按關掉
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
            
    # 背景顏色
    screen.fill(WHITE)
    # 畫出所有角色
    block_list.draw(screen)
    # 更新 
    pygame.display.flip()
    clock.tick(60)

#程式結束
pygame.quit()
    

