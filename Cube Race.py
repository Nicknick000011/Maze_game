from typing import Sequence

import pygame
import time

load = True

pygame.init()
scr = pygame.display.set_mode((1370, 770))
bc = (10, 10, 10)
done = True
y = 65
y2 = 65
x = 65
x2 = 65

timer2 = time.time()
timer4 = time.time()
score = 0
score2 = 0

while done:
    scr.fill(bc)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False

    file = open("highscore.txt","r")
    h = file.read()
    file.close()

    file2 = open("toohigh.txt","r")
    h2 = file2.read()
    file2.close()

    pygame.draw.circle(scr, (33, 33, 33), [80, 80], 40, 0)  # p1
    wallu = pygame.draw.rect(scr, (30, 0, 0), pygame.Rect(0, 0, 1550, 20))  # outlines
    wallr = pygame.draw.rect(scr, (30, 0, 0), pygame.Rect(0, 0, 20, 6554))
    walll = pygame.draw.rect(scr, (30, 0, 0), pygame.Rect(0, 750, 1550, 20))
    walld = pygame.draw.rect(scr, (30, 0, 0), pygame.Rect(1350, 0, 20, 6554))
    win = pygame.draw.circle(scr, (33, 33, 0), [1166, 685], 30, 0)  # win
    wall0 = pygame.draw.rect(scr, (30, 0, 0), pygame.Rect(0, 180, 250, 20))
    wall1 = pygame.draw.rect(scr, (30, 0, 0), pygame.Rect(550, 180, 20, 720))
    wall2 = pygame.draw.rect(scr, (30, 0, 0), pygame.Rect(350, 5, 20, 570))
    wall3 = pygame.draw.rect(scr, (30, 0, 0), pygame.Rect(1100, 180, 20, 580))
    wall4 = pygame.draw.rect(scr, (30, 0, 0), pygame.Rect(800, 0, 20, 660))
    wall5 = pygame.draw.rect(scr, (30, 0, 0), pygame.Rect(111, 333, 330, 20))  # 1st elevator
    wall6 = pygame.draw.rect(scr, (30, 0, 0), pygame.Rect(15, 444, 240, 20))  # so on
    wall7 = pygame.draw.rect(scr, (30, 0, 0), pygame.Rect(111, 555, 240, 20))
    wall8 = pygame.draw.rect(scr, (30, 0, 0), pygame.Rect(15, 667, 240, 99))
    wall9 = pygame.draw.rect(scr, (30, 0, 0), pygame.Rect(900, 500, 200, 20))
    wall10 = pygame.draw.rect(scr, (30, 0, 0), pygame.Rect(650, 400, 350, 20))
    wall11 = pygame.draw.rect(scr, (30, 0, 0), pygame.Rect(470, 180, 250, 20))
    wall12 = pygame.draw.rect(scr, (30, 0, 0), pygame.Rect(440, 580, 280, 20))
    wall13 = pygame.draw.rect(scr, (30, 0, 0), pygame.Rect(900, 300, 333, 20))
    wall14 = pygame.draw.rect(scr, (30, 0, 0), pygame.Rect(800, 200, 200, 20))
    wall15 = pygame.draw.rect(scr, (30, 0, 0), pygame.Rect(1200, 450, 333, 20))
    wall16 = pygame.draw.rect(scr, (30, 0, 0), pygame.Rect(1100, 600, 160, 20))
    p1 = pygame.draw.rect(scr, (55, 0, 55), pygame.Rect(x, y, 30, 30))
    p2 = pygame.draw.rect(scr, (0, 55, 0), pygame.Rect(x2, y2, 30, 30))

    press2 = pygame.key.get_pressed()

    if press2[pygame.K_UP] or press2[pygame.K_DOWN]:
        if press2[pygame.K_UP]:
            y2 = y2 - 1.1
        if press2[pygame.K_DOWN]:
            y2 = y2 + 1.1
    if press2[pygame.K_RIGHT] or press2[pygame.K_LEFT]:
        if press2[pygame.K_RIGHT]:
            x2 = x2 + 1.1
        if press2[pygame.K_LEFT]:
            x2 = x2 - 1.1

    press = pygame.key.get_pressed()

    if press[pygame.K_w] or press[pygame.K_s]:
        if press[pygame.K_w]:
            y = y - 1.1
        if press[pygame.K_s]:
            y = y + 1.1
    if press[pygame.K_d] or press[pygame.K_a]:
        if press[pygame.K_d]:
            x = x + 1.1
        if press[pygame.K_a]:
            x = x - 1.1

    if p1.colliderect(wallu):
        wtouch()
    elif p1.colliderect(wallr):
        wtouch()
    elif p1.colliderect(walld):
        wtouch()
    elif p1.colliderect(walll):
        wtouch()

    if p2.colliderect(wallu):
        wtouch2()
    elif p2.colliderect(wallr):
        wtouch2()
    elif p2.colliderect(walld):
        wtouch2()
    elif p2.colliderect(walll):
        wtouch2()


    def wtouch():
        global x, y
        if press[pygame.K_w] or press[pygame.K_s]:
            if press[pygame.K_w]:
                y = y + 3
            elif press[pygame.K_s]:
                y = y - 3
        if press[pygame.K_d] or press[pygame.K_a]:
            if press[pygame.K_d]:
                x = x - 3
            elif press[pygame.K_a]:
                x = x + 3

    def wtouch2():
        global x2, y2
        if press2[pygame.K_UP] or press2[pygame.K_DOWN]:
            if press2[pygame.K_UP]:
                y2 = y2 + 3
            if press[pygame.K_DOWN]:
                y2 = y2 - 3
        if press2[pygame.K_LEFT] or press2[pygame.K_RIGHT]:
           if press2[pygame.K_RIGHT]:
                x2 = x2 - 3
           if press2[pygame.K_LEFT]:
               x2 = x2 + 3

    if p1.colliderect(wall0): wtouch()
    if p1.colliderect(wall1): wtouch()
    if p1.colliderect(wall2): wtouch()
    if p1.colliderect(wall3): wtouch()
    if p1.colliderect(wall4): wtouch()
    if p1.colliderect(wall5): wtouch()
    if p1.colliderect(wall6): wtouch()
    if p1.colliderect(wall7): wtouch()
    if p1.colliderect(wall8): wtouch()
    if p1.colliderect(wall9): wtouch()
    if p1.colliderect(wall10): wtouch()
    if p1.colliderect(wall11): wtouch()
    if p1.colliderect(wall12): wtouch()
    if p1.colliderect(wall13): wtouch()
    if p1.colliderect(wall14): wtouch()
    if p1.colliderect(wall15): wtouch()
    if p1.colliderect(wall16): wtouch()
    if p1.colliderect(win):
        y = 56
        x = 56
        timer = time.time()
        score = round(timer - timer2, 2)
        timer2 = time.time()
        print("p1 gets a time of", score)

    if p2.colliderect(win):
        x2 = 56
        y2 = 120
        timer3 = time.time()
        score2 = round(timer3 - timer4, 2)
        timer4 = time.time()
        print("p2 gets a time of", score2)

    if p2.colliderect(wall0): wtouch2()
    if p2.colliderect(wall1): wtouch2()
    if p2.colliderect(wall2): wtouch2()
    if p2.colliderect(wall3): wtouch2()
    if p2.colliderect(wall4): wtouch2()
    if p2.colliderect(wall5): wtouch2()
    if p2.colliderect(wall6): wtouch2()
    if p2.colliderect(wall7): wtouch2()
    if p2.colliderect(wall8): wtouch2()
    if p2.colliderect(wall9): wtouch2()
    if p2.colliderect(wall10): wtouch2()
    if p2.colliderect(wall11): wtouch2()
    if p2.colliderect(wall12): wtouch2()
    if p2.colliderect(wall13): wtouch2()
    if p2.colliderect(wall14): wtouch2()
    if p2.colliderect(wall15): wtouch2()
    if p2.colliderect(wall16): wtouch2()

    font_timer1 = pygame.font.SysFont("tahoma", 30, True, True)
    text_timer1 = font_timer1.render("P1 Time:" + str(score), True, (255, 255, 255))
    scr.blit(text_timer1, (1100, 30))

    font_timer1 = pygame.font.SysFont("tahoma", 30, True, True)
    text_timer1 = font_timer1.render("P2 Time:" + str(score2), True, (255, 255, 255))
    scr.blit(text_timer1, (1100, 70))

    if float(score) < float(h) and score > 0:
        file = open("highscore.txt","w")
        file.write(str(score))
        file.close()

    if float(score2) < float(h) and score2 > 0:
        file2 = open("toohigh.txt", "w")
        file2.write(str(score2))
        file2.close()


    pygame.display.flip()
