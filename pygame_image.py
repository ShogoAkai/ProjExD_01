import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01-20230926/fig/pg_bg.jpg")
    kk_img= pg.image.load("ex01-20230926/fig/3.png")
    kk_img = pg.transform.flip(kk_img, True, False)
    kk_imgs = pg.transform.rotozoom(kk_img, 10, 1.0)
    kk_image3 = pg.transform.rotozoom(kk_img, 3, 1.0)
    kk_image4 = pg.transform.rotozoom(kk_img, 4, 1.0)
    kk_image5 = pg.transform.rotozoom(kk_img, 5, 1.0)
    kk_image6 = pg.transform.rotozoom(kk_img, 6, 1.0)
    kk_image7 = pg.transform.rotozoom(kk_img, 7, 1.0)
    kk_image8 = pg.transform.rotozoom(kk_img, 8, 1.0)
    kk_image9 = pg.transform.rotozoom(kk_img, 9, 1.0)
    kk_image10 = pg.transform.rotozoom(kk_img, 10, 1.0)
    kk_imgs = [kk_img, kk_imgs, kk_image3,kk_image4, kk_image5, kk_image6, kk_image7, kk_image8, kk_image9, kk_image10]
    #kk_imgs = [kk_img, kk_imgs]
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        x=-tmr
        screen.blit(bg_img, [1600-x, 0])
        screen.blit(kk_img[tmr%2], [300,200])
        pg.display.update()
        tmr += 1        
        clock.tick(100)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()