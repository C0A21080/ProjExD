from random import randint
import pygame as pg
import sys

def main():
    clock = pg.time.Clock()

    #練習1　スクリーンと背景画像
    pg.display.set_caption("逃げろ！こうかとん")
    screen_sfc = pg.display.set_mode((1600, 900)) #Surface
    screen_rct = screen_sfc.get_rect() #Rect
    bgimg_sfc = pg.image.load("fig/pg_bg.jpg") #Surface
    bgimg_rct = bgimg_sfc.get_rect() #Rect
    screen_sfc.blit(bgimg_sfc, bgimg_rct)

    #練習3　こうかとん
    kkimg_sfc = pg.image.load("fig/4 .png") #Surface
    kkimg_sfc = pg.transform.rotozoom(kkimg_sfc, 0, 2.0) #Surface
    kkimg_rct = kkimg_sfc.get_rect() #Rect
    kkimg_rct.center = 900, 400

    #練習5  爆弾
    bm1img_sfc = pg.Surface((20, 20)) #Surface
    bm1img_sfc.set_colorkey((0, 0, 0))
    pg.draw.circle(bm1img_sfc, (255, 0, 0), (10, 10), 10)
    bm1img_rct = bm1img_sfc.get_rect() #Rect
    bm1img_rct.centerx = randint(0, screen_rct.width)
    bm1img_rct.centery = randint(0, screen_rct.height)
    vx1, vy1 = +3, +3 #練習6

    bm2img_sfc = pg.Surface((20, 20)) #Surface
    bm2img_sfc.set_colorkey((0, 0, 0))
    pg.draw.circle(bm2img_sfc, (0, 0, 255), (10, 10), 1000)
    bm2img_rct = bm2img_sfc.get_rect() #Rect
    bm2img_rct.centerx = randint(0, screen_rct.width)
    bm2img_rct.centery = randint(0, screen_rct.height)
    vx2, vy2 = +3, +3


    while True:
        screen_sfc.blit(bgimg_sfc, bgimg_rct)

        #練習2
        for event in pg.event.get():
            if event.type == pg.QUIT:return
            
        #練習4
        key_states = pg.key.get_pressed() #辞書
        if key_states[pg.K_UP]    == True: kkimg_rct.centery -= 10
        if key_states[pg.K_DOWN]  == True: kkimg_rct.centery += 10
        if key_states[pg.K_LEFT]  == True: kkimg_rct.centerx -= 10
        if key_states[pg.K_RIGHT] == True: kkimg_rct.centerx += 10

        if key_states[pg.K_UP]    == True: bm1img_rct.centery -= 10
        if key_states[pg.K_DOWN]  == True: bm1img_rct.centery += 10
        if key_states[pg.K_LEFT]  == True: bm1img_rct.centerx -= 10
        if key_states[pg.K_RIGHT] == True: bm1img_rct.centerx += 10

        if key_states[pg.K_UP]    == True: bm2img_rct.centery += 15
        if key_states[pg.K_DOWN]  == True: bm2img_rct.centery -= 15
        if key_states[pg.K_LEFT]  == True: bm2img_rct.centerx += 15
        if key_states[pg.K_RIGHT] == True: bm2img_rct.centerx -= 15
        #練習7
        if check_bound(kkimg_rct, screen_rct) != (1, 1): #領域外だったら
            if key_states[pg.K_UP]    == True: kkimg_rct.centery += 100
            if key_states[pg.K_DOWN]  == True: kkimg_rct.centery -= 100
            if key_states[pg.K_LEFT]  == True: kkimg_rct.centerx += 100
            if key_states[pg.K_RIGHT] == True: kkimg_rct.centerx -= 100
        screen_sfc.blit(kkimg_sfc, kkimg_rct)

        #練習6
        bm1img_rct.move_ip(vx1, vy1)
        bm2img_rct.move_ip(vx2, vy2)
        #練習5
        screen_sfc.blit(bm1img_sfc, bm1img_rct)
        screen_sfc.blit(bm2img_sfc, bm2img_rct)
        #練習7
        yoko, tate = check_bound(bm1img_rct, screen_rct)
        vx1 *= yoko
        vy1 *= tate

        yoko, tate = check_bound(bm2img_rct, screen_rct)
        vx2 *= yoko
        vy2 *= tate

        #練習8
        if kkimg_rct.colliderect(bm1img_rct): return

        pg.display.update()
        clock.tick(1000)
        if kkimg_rct.colliderect(bm2img_rct): return

        pg.display.update()
        clock.tick(1000)

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
