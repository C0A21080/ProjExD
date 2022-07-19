from random import randint
import pygame as pg
import sys

def main():
    clock = pg.time.Clock()

    #練習1　スクリーンと背景画像
    pg.display.set_caption("ikiろ！こうかとん")
    screen_sfc = pg.display.set_mode((1600, 900)) #Surface
    screen_rct = screen_sfc.get_rect() #Rect
    bgimg_sfc = pg.image.load("fig/mori.jpeg") #Surface
    bgimg_sfc = pg.transform.rotozoom(bgimg_sfc, 0, 2.65)#Surface
    bgimg_rct = bgimg_sfc.get_rect() #Rect
    screen_sfc.blit(bgimg_sfc, bgimg_rct)

    #練習3　こうかとん
    kkimg_sfc = pg.image.load("fig/4dot.png") #Surface
    kkimg_sfc = pg.transform.rotozoom(kkimg_sfc, 0, 2.0) #Surface
    kkimg_rct = kkimg_sfc.get_rect() #Rect
    kkimg_rct.center = 900, 400

    #練習5  爆弾
    fdimg_sfc = pg.image.load("fig/mushi.png") #Surface
    fdimg_sfc = pg.transform.rotozoom(kkimg_sfc, 0, 1.0) #Surface
    fdimg_rct = fdimg_sfc.get_rect() #Rect
    fdimg_rct.centerx = randint(0, screen_rct.width)
    fdimg_rct.centery = randint(0, screen_rct.height)

    while True:
        screen_sfc.blit(bgimg_sfc, bgimg_rct)

        #練習2
        for event in pg.event.get():
            if event.type == pg.QUIT:return
            
        #練習4
        key_states = pg.key.get_pressed() #辞書
        if key_states[pg.K_UP]    == True: kkimg_rct.centery -= 20
        if key_states[pg.K_DOWN]  == True: kkimg_rct.centery += 20
        if key_states[pg.K_LEFT]  == True: kkimg_rct.centerx -= 20
        if key_states[pg.K_RIGHT] == True: kkimg_rct.centerx += 20

        #練習7
        if check_bound(kkimg_rct, screen_rct) != (1, 1): #領域外だったら
            if key_states[pg.K_UP]    == True: kkimg_rct.centery += 20
            if key_states[pg.K_DOWN]  == True: kkimg_rct.centery -= 20
            if key_states[pg.K_LEFT]  == True: kkimg_rct.centerx += 20
            if key_states[pg.K_RIGHT] == True: kkimg_rct.centerx -= 20
        screen_sfc.blit(kkimg_sfc, kkimg_rct)

        #練習6
        fdimg_rct.move_ip(vx, vy)
        #練習5
        screen_sfc.blit(fdimg_sfc, fdimg_rct)
        #練習7
        yoko, tate = check_bound(fdimg_rct, screen_rct)
        vx *= yoko
        vy *= tate

        #練習8
        if kkimg_rct.colliderect(fdimg_rct): return

        pg.display.update()
        clock.tick(1000)

       # pg.display.update()
        #clock.tick(1000)

#練習7
def check_bound(rct, scr_rct):
    '''
    [1]rct:こうかとんor爆弾のRect
    [2]scr_rct:スクリーンのRect
    '''
    yoko, tate = +1, +1 #領域内
    if rct.left < scr_rct.left or scr_rct.right < rct.right: yoko = -1 #領域外
    if rct.top < scr_rct.top or scr_rct.bottom < rct.bottom: tate = -1 #領域外
    return yoko, tate


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
