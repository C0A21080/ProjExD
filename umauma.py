import pygame as pg
import sys
import random


width = 2000

class Screen:
    def __init__(self, title, wh, image):
        pg.display.set_caption(title)
        self.sfc = pg.display.set_mode(wh)     # Surface
        self.rct = self.sfc.get_rect()         # Rect
        self.bgi_sfc = pg.image.load(image)    # Surface
        self.bgi_rct = self.bgi_sfc.get_rect() # Rect

    def blit(self):
        self.sfc.blit(self.bgi_sfc, self.bgi_rct)


class Bird:
    def __init__(self, image: str, size: float, xy):
        self.sfc = pg.image.load(image)    # Surface
        self.sfc = pg.transform.rotozoom(self.sfc, 0, size)  # Surface
        self.rct = self.sfc.get_rect()          # Rect
        self.rct.center = xy

    def blit(self, scr: Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr: Screen):
        key_states = pg.key.get_pressed() # 辞書
        if key_states[pg.K_UP]: 
            self.rct.centery -= 2
        if key_states[pg.K_DOWN]: 
            self.rct.centery += 2
        if key_states[pg.K_LEFT]: 
            self.rct.centerx -= 2
        if key_states[pg.K_RIGHT]: 
            self.rct.centerx += 2
            
        # # 練習7
        if check_bound(self.rct, scr.rct) != (1, 1): # 領域外だったら
            if key_states[pg.K_UP]: 
                self.rct.centery += 1
            if key_states[pg.K_DOWN]: 
                self.rct.centery -= 1
            if key_states[pg.K_LEFT]: 
                self.rct.centerx += 1
            if key_states[pg.K_RIGHT]: 
                self.rct.centerx -= 1
        self.blit(scr)
    



class food:
    def __init__(self, color, size, vxy, scr: Screen):
        global width
        self.sfc = pg.Surface((2*size, 2*size)) # Surface
        self.sfc.set_colorkey((0, 0, 0)) 
        pg.draw.circle(self.sfc, color, (size, size), size)
        self.rct = self.sfc.get_rect() # Rect
        self.rct.centerx = 1700+random.randint(10,1000)
        self.rct.centery = random.randint(0, scr.rct.height)
        self.vx, self.vy = vxy 

    def blit(self, scr: Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr: Screen):
        self.rct.move_ip(self.vx, self.vy)
        self.blit(scr)   
        if  self.rct.centerx <0 :
             self.rct.centerx = 1700+random.randint(10,1000)

class bomb:
    def __init__(self, color, size, vxy, scr: Screen):
        global width
        self.sfc = pg.Surface((2*size, 2*size)) # Surface
        self.sfc.set_colorkey((0, 0, 0)) 
        pg.draw.circle(self.sfc, color, (size, size), size)
        self.rct = self.sfc.get_rect() # Rect
        self.rct.centerx = random.randint(0, scr.rct.width)
        self.rct.centery = -random.randint(0,1000)
        self.vx, self.vy = vxy 

    def blit(self, scr: Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr: Screen):
        self.rct.move_ip(self.vx, self.vy)
        self.blit(scr)   
        if  self.rct.centery >scr.rct.height :
              self.rct.centery = -random.randint(0,1000)
        



def main():
    a=2
    font = pg.font.Font(None, 55)
    score = 0
    clock = pg.time.Clock()
    scr = Screen("見分けろ！こうかとん", (1600, 900), "fig/pg_bg.jpg")
    kkt = Bird("fig/4dot.png", a, (900, 400))
    food1= food((255,255,0), 30, (-1,0), scr)#一つ目の餌を作成
    food2= food((255,255,0), 30, (-1,0), scr)#二つ目の餌を作成
    food3= food((255,255,0), 30, (-1,0), scr)#三つ目の餌を作成
    bomb1=bomb((255,0,0),30,(0,+1),scr)#一つ目の爆弾
    bomb2=bomb((255,0,0),30,(0,+1),scr)#二つ目の爆弾
    bomb3=bomb((255,0,0),30,(0,+1),scr)#三つ目の爆弾

 

    while True:
        scr.blit()
        text = font.render(str(score), True, (255,0,0))   # 描画する文字列の設定
        scr.sfc.blit(text, [1600//2, 100])

        # 練習2
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return


        kkt.update(scr)
        food1.update(scr)
        food2.update(scr)
        food3.update(scr)
        bomb1.update(scr)
        bomb2.update(scr)
        bomb3.update(scr)

        if kkt.rct.colliderect(food1.rct):#一つ目の餌と当たった時にスコアを＋１して餌を画面外に移動
            score += 1
            food1= food((255,255,0), 30, (-1,0), scr)
        
        if kkt.rct.colliderect(food2.rct):##二つ目の餌と当たった時にスコアを＋１して餌を画面外に移動
            score += 1
            food2= food((255,255,0), 30, (-1,0), scr)
        
        if kkt.rct.colliderect(food3.rct):##三つ目の餌と当たった時にスコアを＋１して餌を画面外に移動
            score += 1
            food3= food((255,255,0), 30, (-1,0), scr)

        if score<10:
            a=5
        
            if kkt.rct.colliderect(bomb1.rct):##一つ目の爆弾と当たった時にスコアを-１して餌を画面外に移動
                score-=1
                bomb1=bomb((255,0,0),30,(0,a),scr)
        
            if kkt.rct.colliderect(bomb2.rct):#二つ目の爆弾と当たった時にスコアを-１して餌を画面外に移動
                score-=1
                bomb2=bomb((255,0,0),30,(0,a),scr)

            if kkt.rct.colliderect(bomb3.rct):##三つ目の爆弾と当たった時にスコアを-１して餌を画面外に移動
                score-=1
                bomb3=bomb((255,0,0),30,(0,a),scr)

            pg.display.update()

        if score>=10:
            a=10

            if kkt.rct.colliderect(bomb1.rct):##一つ目の爆弾と当たった時にスコアを-１して餌を画面外に移動
                score-=100
                bomb1=bomb((255,0,0),30,(0,a),scr)
        
            if kkt.rct.colliderect(bomb2.rct):#二つ目の爆弾と当たった時にスコアを-１して餌を画面外に移動
                score-=100
                bomb2=bomb((255,0,0),30,(0,a),scr)

            if kkt.rct.colliderect(bomb3.rct):##三つ目の爆弾と当たった時にスコアを-１して餌を画面外に移動
                score-=100
                bomb3=bomb((255,0,0),30,(0,a),scr)

            pg.display.update()
        
        if score<0:#スコアがマイナスになったらゲームを強制終了
            return 


        pg.display.update()
        clock.tick(1000)

def check_bound(rct, scr_rct):
    '''
    [1] rct: こうかとん or 爆弾のRect
    [2] scr_rct: スクリーンのRect
    '''
    yoko, tate = +1, +1 # 領域内
    if rct.left < scr_rct.left or scr_rct.right  < rct.right :
        yoko = -1 # 領域外
    if rct.top  < scr_rct.top  or scr_rct.bottom < rct.bottom:
        tate = -1 # 領域外
    return yoko, tate


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()