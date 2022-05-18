import pygame as pg
import time
import random

pg.init()



#create display window
size = (650,350)
screen = pg.display.set_mode(size)
# Set title to the window
pg.display.set_caption("frog")
pg.display.flip()

score = 0
level = 1
num = -25
n = 400
f = 20
rock = 0
rock2 = 0
rock3 = 0
z = 650
q = 10
ab = 0
gerlod_jump = 0

def levels(score, level):
    global rock2
    global ab 
    
    if score <= 500:
        level = 1
        n = random.randint(400,500)
        f = n/20
        f = int(f)
    elif score <= 1000:
        level = 2
        n = random.randint(300,400)
        f = n/20
        f = int(f)
        
    elif score <= 1500:
        level = 3
        n = random.randint(200,300)
        f = n/20
        f = int(f)
    elif score <= 2000:
        level = 4
        n = random.randint(150,300)
        f = n/20
        f = int(f)
    if rock2 == 0:
        rock2 = 1
        ab = 305
    
    difcult = {
        1:10,
        2:12,
        3:15,
        4:17
    }
        

    q = difcult[level]
    global rock
    rock = 0
    global z
    z = 650

    walk(num,n,score,f,q)

def end (score):
    #csv = csv.reader('highscore.csv')
    #high_score = csv["score"]
    #if score >= high_score:
    #    with open('highscore.csv', 'a', newline='') as file:
    #        writer = csv.writer(file)
    #        writer.writerow([score])
    Font = pg.font.Font("Consolas.ttf", 16)
    white = (255, 255, 255)

    text = ("score:" + str(score))
    text = Font.render(text,True, white)
    title = text.get_rect()
    title.center = (330,165)
    screen.blit(text,title)
    pg.display.flip()
    time.sleep(2)
    menu()



def check_pos(y,score,level):
    if y > 200:
        end(score)
    elif y <= 200:
        print ("win")
        
        levels(score,level)

def check_n(n,y,score,level):
    if n == 30:
        pass
        print ("jump")
        #display rocks
    print (n)

    if n == None:
        print ("erro")

    if n  <=  0:
        print ("end")
        check_pos(y,score,level)

    
            
        



def display_background(num,n,y,score,level,f,q):
    check_n (n,y,score,level)
    background_image = pg.image.load("bg.png").convert()
    background_image = pg.transform.rotozoom(background_image, 0, 2)
    screen.blit(background_image, [0, 0])
    frame1 = pg.image.load("bg_frames/1.png")
    frame2 = pg.image.load("bg_frames/2.png")
    frame3 =  pg.image.load("bg_frames/3.png")
    frame4 = pg.image.load("bg_frames/4.png")
    frame5 = pg.image.load("bg_frames/5.png")
    frame6 = pg.image.load("bg_frames/6.png")
    frame7 = pg.image.load("bg_frames/7.png")
    frame8 = pg.image.load("bg_frames/8.png")
    frame9 = pg.image.load("bg_frames/9.png")
    frame10 = pg.image.load("bg_frames/10.png")
    frame11 = pg.image.load("bg_frames/2.png")
    check_n(n,y,score,level)

    Font = pg.font.Font("Consolas.ttf", 16)
    white = (255, 255, 255)
    

    run = True
    
    if run == True:
        global rock
        #screen.blit(background_image, [0,0])
        screen.blit(frame1, [0, 0])
        screen.blit(frame3, [0, 45])

        screen.blit(frame1, [num, 0])
        screen.blit(frame7, [num, 45])
        if num >= 625:
            num = num - 700
        num = num + 50
        screen.blit(frame2, [num, 0])
        screen.blit(frame8, [num, 45])
        if num >= 625:
            num = num - 700
        num = num + 50
        screen.blit(frame3, [num, 0])
        screen.blit(frame9, [num, 45])
        if num >= 625:
            num = num - 700
        num = num + 50
        screen.blit(frame4, [num, 0])
        screen.blit(frame10, [num, 45])
        if num >= 625:
            num = num - 700
        num = num + 50
        screen.blit(frame5, [num, 0])
        screen.blit(frame11, [num, 45])
        if num >= 625:
            num = num - 700
        num = num + 50
        screen.blit(frame6, [num, 0])
        screen.blit(frame1, [num, 45])
        if num >= 625:
            num = num - 700
        num = num + 50
        screen.blit(frame7, [num, 0])
        screen.blit(frame2, [num, 45])
        if num >= 625:
            num = num - 700
        num = num + 50
        screen.blit(frame8, [num, 0])
        screen.blit(frame3, [num, 45])
        if num >= 625:
            num = num - 700
        num = num + 50
        screen.blit(frame9, [num, 0])
        screen.blit(frame4, [num, 45])
        if num >= 625:
            num = num - 700
        num = num + 50
        screen.blit(frame10, [num, 0])
        screen.blit(frame5, [num, 45])
        if num >= 625:
            num = num - 700
        num = num + 50
        screen.blit(frame11, [num, 0])
        screen.blit(frame6, [num, 45])
        if num >= 625:
            num = num -700
        num = num + 50
        screen.blit(frame4, [num, 0])
        screen.blit(frame11, [num, 45])
        if num >= 625:
            num = num - 700
        num = num + 50
        screen.blit(frame5, [num, 0])
        screen.blit(frame10, [num, 45])
        if num >= 625:
            num = num - 700
        num = num + 50
        screen.blit(frame6, [num, 0])
        screen.blit(frame9, [num, 45])
        if num >= 625:
            num = num -700
        num = num + 50
        num = num - 5
        global rock
        global rock2
        global rock3
        rock = 1
        if n <= 110:
            rock = 1
        else:
            rock = 0
        
        if rock == 1:
            rocks = pg.image.load("rocks!!!.png")
            global z
            screen.blit(rocks, [z, 240])
            z = z - 15
            rocks = pg.image.load("rocks!!!.png")
            print ("rocks:",z)
        if rock2 == 1:
            global gerlod_jump
            rocks = pg.image.load("rocks!!!.png")
            global ab
            screen.blit(rocks, [ab, 240])
            ab = ab - 15
            rocks = pg.image.load("rocks!!!.png")
            if ab <= 0:
                gerlod_jump = 0
                rock2 = 0
                
            if ab <= 110:
                if gerlod_jump == 0:
                    x = ab
                    jump('gerlod', 50, 'bob', 315, num,n,score,x,q)
                    gerlod_jump = 1
                    
                
            
        text = ("score:" + str(score))
        text = Font.render(text,True, white)
        title = text.get_rect()
        title.center = (600,50)
        screen.blit(text,title)



        #   pg.display.flip()

    return num


def jump (frogname,x,frog,x1,num,n,score,f,q):
    clock = pg.time.Clock()
    display_background(num,n,230,score,level,f,q)

    frog1 = frogname + "/walk1.png"
    frog2 = frogname + "/walk2.png"
    frog3 = frogname + "/walk3.png" 

    walk1 = pg.image.load (frog1)
    walk2 = pg.image.load (frog2)
    walk3 = pg.image.load (frog3)

    frog_1 = frog + "/walk1.png"
    frog_2 = frog + "/walk2.png"
    frog_3 = frog + "/walk3.png"

    walk_1 = pg.image.load (frog_1)
    walk_2 = pg.image.load (frog_2)
    walk_3 = pg.image.load (frog_3)
    
    display_background(num,n,190,score,level,f,q)
    screen.blit(walk3, (x, 190))
    screen.blit(walk_1, (x1, 220))
    num = num - 5
    n = n - 5
    pg.display.flip()
    clock.tick(q)
    display_background(num,n,180,score,level,f,q)
    screen.blit(walk3, (x, 180))
    screen.blit(walk_2, (x1, 220))
    num = num - 5
    n = n - 5
    pg.display.flip()
    clock.tick(q)
    display_background(num,n,170,score,level,f,q)
    screen.blit(walk3, (x, 170))
    screen.blit(walk_3, (x1, 220))
    num = num -5
    n = n -5
    pg.display.flip()

    clock.tick(q)
    display_background(num,n,185,score,level,f,q)
    screen.blit(walk2,(x,185))
    screen.blit(walk_1, (x1, 220))
    num = num - 5
    pg.display.flip()
    clock.tick(q)
    display_background(num,n,195,score,level,f,q)
    screen.blit(walk2,(x,195))
    screen.blit(walk_2, (x1, 220))
    num = num - 5
    n = n - 5
    pg.display.flip()
    clock.tick(q)
    display_background(num,n,200,score,level,f,q)
    screen.blit(walk1,(x,200))
    screen.blit(walk_3, (x1, 220))
    num = num - 5
    n = n - 5

    pg.display.flip()
    score = int(score) + 15
    f = f - 1
    walk(num,n,score,f,q)


    pg.display.flip()

def walk(num,n,score,f,q):
    walks = True
    clock = pg.time.Clock()

    
    frog1 = "bob/walk1.png"
    frog2 = "bob/walk2.png"
    frog3 = "bob/walk3.png"

    frog_1 = "gerlod/walk1.png"
    frog_2 = "gerlod/walk2.png"
    frog_3 = "gerlod/walk3.png"

    walk1 = pg.image.load (frog1)
    walk2 = pg.image.load (frog2)
    walk3 = pg.image.load (frog3)

    walk_1 = pg.image.load (frog_1)
    walk_2 = pg.image.load (frog_2)
    walk_3 = pg.image.load (frog_3)
    
    for x in range(f):
        clock.tick(q)
        num = display_background(num,n,220,score,level,f,q)
        screen.blit(walk1, (310, 220))
        screen.blit(walk_1, (60, 220))
        pg.display.flip()
        num = num - 5
        n = n - 5
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                jump('bob', 315, 'gerlod', 50, num,n,score,x,q)
        clock.tick(q)
        num = display_background(num,n,220,score,level,f,q)
        screen.blit(walk2, (315, 220))
        screen.blit(walk_2, (55, 220))
        pg.display.flip()
        num = num - 5
        n = n -5
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                jump('bob', 315, 'gerlod', 50, num,n,score,x,q)
        clock.tick(q)
        num = display_background(num,n,220,score,level,f,q)
        screen.blit(walk3,(320,220))
        screen.blit(walk_3,(50,220))
        pg.display.flip()
        num = num - 5
        n = n - 5
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                jump('bob', 315, 'gerlod', 50, num,n,score,x,q)
        clock.tick(q)
        display_background(num,n,220,score,level,f,q)
        screen.blit(walk2, (315, 220))
        screen.blit(walk_2, (50, 220))
        pg.display.flip()
        num = num - 5
        n = n - 5
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                jump('bob', 315, 'gerlod', 50, num,n,score,x,q)
        score = score + 10
    if n <=  0:
        end(score)
    else:
        f = 1
        walk(num,n,score,f,q)
    
    

def menu ():
    menu = True
    score = 0
    level = 1
    num = -25
    n = 400
    f = 20
    q = 10
    y = 0

    global rock
    rock = 0
    global z
    z = 650
    
    display_background(num,n,y,score,level,f,q)
    frog1 = "bob/walk1.png"
    frog2 = "bob/walk2.png"
    frog3 = "bob/walk3.png"

    frog_1 = "gerlod/walk1.png"
    frog_2 = "gerlod/walk2.png"
    frog_3 = "gerlod/walk3.png"

    walk1 = pg.image.load (frog1)
    walk2 = pg.image.load (frog2)
    walk3 = pg.image.load (frog3)

    walk_1 = pg.image.load (frog_1)
    walk_2 = pg.image.load (frog_2)
    walk_3 = pg.image.load (frog_3)
    clock = pg.time.Clock()
    white = (255, 255, 255)
    Font = pg.font.Font("Consolas.ttf", 16)
    text = ("press space to start and jump")
    text = Font.render(text,True, white)
    
    while menu == True:
        clock.tick(q)
        title = text.get_rect()
        title.center = (330,165)
        screen.blit(text,title)
        num = display_background(num,n,220,score,level,f,q)
        screen.blit(walk1, (470, 220))
        screen.blit(walk_1, (90, 220))
        pg.display.flip()
        screen.blit(text,title)
        title = text.get_rect()
        num = num - 5
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                walk(num,n,score,f,q)

        clock.tick(q)
        num = display_background(num,n,220,score,level,f,q)
        title.center = (330,165)
        screen.blit(text,title)
        screen.blit(walk2, (475, 220))
        screen.blit(walk_2, (95, 220))
        pg.display.flip()
        num = num - 5
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                walk(num,n,score,f,q)

        clock.tick(q)
        num = display_background(num,n,220,score,level,f,q)
        title.center = (330,165)
        screen.blit(text,title)
        screen.blit(walk3,(470,220))
        screen.blit(walk_3,(90,220))
        pg.display.flip()
        title = text.get_rect()
        num = num - 5
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                walk(num,n,score,f,q)

        clock.tick(q)
        display_background(num,n,220,score,level,f,q)
        title.center = (330,165)
        screen.blit(text,title)
        screen.blit(walk2, (475, 220))
        screen.blit(walk_2, (90, 220))
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                walk(num,n,score,f,q)
        pg.display.flip()
        num = num - 5

    

menu()