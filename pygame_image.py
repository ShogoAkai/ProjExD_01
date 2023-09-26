import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01-20230926/fig/pg_bg.jpg")
    kk_image= pg.image.load("ex01-20230926/fig/3.png")
    kk_image = pg.transform.flip(kk_image, True, False)
    kk_image2 = pg.transform.rotozoom(kk_image, 2, 1.0)
    kk_image3 = pg.transform.rotozoom(kk_image, 3, 1.0)
    kk_image4 = pg.transform.rotozoom(kk_image, 4, 1.0)
    kk_image5 = pg.transform.rotozoom(kk_image, 5, 1.0)
    kk_image6 = pg.transform.rotozoom(kk_image, 6, 1.0)
    kk_image7 = pg.transform.rotozoom(kk_image, 7, 1.0)
    kk_image8 = pg.transform.rotozoom(kk_image, 8, 1.0)
    kk_image9 = pg.transform.rotozoom(kk_image, 9, 1.0)
    kk_image10 = pg.transform.rotozoom(kk_image, 10, 1.0)
    kk_images = [kk_image, kk_image2, kk_image3,kk_image4, kk_image5, kk_image6, kk_image7, kk_image8, kk_image9, kk_image10]
    kk_images = [kk_image, kk_image2]
    bg_img2=pg.transform.flip(bg_img,True,False)
    tmr = 0
    a=0
    while True:
        kok_img=pg.transform.rotate(bg_img2,a)
        kk_img3=[bg_img2, kok_img]
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        x=tmr%1600
        screen.blit(bg_img, [-x, 0])
        screen.blit(bg_img, [1600-x, 0])
        screen.blit(kk_images[tmr%2], [300, 200])
        pg.display.update()
        tmr += 1   
        clock.tick(100)
        

        

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()