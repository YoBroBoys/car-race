import pygame
import random
pygame.init()
x,y = 612,612

all = (20,200,20)
blu = (199,199,20)
black = (255,255,255)
white = (0,0,0)
grn = (20,100,255)

window = pygame.display.set_mode((x,y))
pygame.display.set_caption("Car Race Game")

bg = pygame.image.load("Assets/Bg.jpg")
maincar = pygame.image.load("Assets/maincar.png")
maincar = pygame.transform.scale(maincar,(150,200))
car1 = pygame.image.load("Assets/car1.png")
car1 = pygame.transform.scale(car1,(100,200))
car2 = pygame.image.load("Assets/car2.png")
car2 = pygame.transform.scale(car2,(100,200))
car3 = pygame.image.load("Assets/car3.png")
car3 = pygame.transform.scale(car3,(100,200))

bgsound = pygame.mixer.Sound('Assets/bg sound.mp3')
crash = pygame.mixer.Sound('Assets/car-crash.mp3')

car_width, car_height = 100, 200
car_speed = 5
cars = []

font = pygame.font.SysFont(None,40)


def text(content,colour,xpos,ypos):
    msg = font.render(content,True,colour)
    window.blit(msg,(xpos,ypos))


def score(score):
    msg = font.render("Score :"+str(score), True, black)
    window.blit(msg, (50,50))


def car():
    type = random.choice(['1','2','3'])
    car_x = random.randint(1,3)
    car_y = -20
    return {'t':type,'x': car_x,'y':car_y}

play = False
def game():
    close_btn = pygame.Rect(50, 50, 50, 50)
    maincar_x = x / 2 - 75
    maincar_y = 400
    a = False
    d = False
    clock = pygame.time.Clock()
    play = True
    while play:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    a = True
                if event.key == pygame.K_d:
                    d = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    a = False
                if event.key == pygame.K_d:
                    d = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousex, mousey = pygame.mouse.get_pos()
                if close_btn.collidepoint(mousex,mousey):
                    menu()

        window.blit(bg, (0, 0))
        pygame.draw.rect(window, black, close_btn)
        text("X", white, 65, 65)
        if a == True and maincar_x > 100-12:
            maincar_x -= 10
        if d == True and maincar_x+150 < 512:
            maincar_x += 10
        if random.random() < 0.01:
            cars.append(car())
        for cara in cars:
            cara['y'] += car_speed

            if cara['y'] > y:
                cara['x'] = random.randint(1,3)
                cara['y'] = -20
            if cara['x'] == 1:
                cposx = 100
            elif cara['x'] == 2:
                cposx = 250
            else:
                cposx = 400
            if cara['t'] == '1':
                window.blit(car1, (cposx, cara['y']))
            elif cara['t'] == '2':
                window.blit(car2, (cposx, cara['y']))
            elif cara['t'] == '3':
                window.blit(car3, (cposx, cara['y']))

            maincar_rect = pygame.Rect(maincar_x,maincar_y,150,200)
            for cara in cars:
                car_rect = pygame.Rect(cposx,cara['y'],car_width,car_height)
                if maincar_rect.colliderect(car_rect):
                    crash.play()
                    play = False
        window.blit(maincar,(maincar_x,maincar_y))
        clock.tick(30)
        pygame.display.update()


def menu():
    play_btn = pygame.Rect(x/2 - 100,200,200,50)
    sett_btn = pygame.Rect(x/2 - 100,300,200,50)
    help_btn = pygame.Rect(x / 2 - 100, 400, 200, 50)

    ran = True
    while ran:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousex, mousey = pygame.mouse.get_pos()
                if play_btn.collidepoint(mousex,mousey):
                    game()
                if sett_btn.collidepoint(mousex, mousey):
                    sett()
                if help_btn.collidepoint(mousex, mousey):
                    helpa()

        window.fill(all)
        text("Car Game", black,x/2 - 75,100)
        pygame.draw.rect(window,black,play_btn)
        pygame.draw.rect(window,black,sett_btn)
        pygame.draw.rect(window, black, help_btn)
        text("Play", white, 275, 210)
        text("Settings", white, 250, 310)
        text("Help", white, 275, 410)
        pygame.display.update()


def sett():
    mu_on_bttn = pygame.Rect(250,200,100,50)
    mu_off_bttn = pygame.Rect(400, 200, 100, 50)
    close_btn = pygame.Rect(50, 50, 50, 50)
    music = True
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousex, mousey = pygame.mouse.get_pos()
                if close_btn.collidepoint(mousex,mousey):
                    menu()
                if mu_on_bttn.collidepoint(mousex,mousey):
                    bgsound.set_volume(1)
                    crash.set_volume(1)
                if mu_off_bttn.collidepoint(mousex,mousey):
                    bgsound.set_volume(0)
                    crash.set_volume(0)



        window.fill(blu)
        text("Settings", black,x/2 - 75,100)
        pygame.draw.rect(window,black,close_btn)
        text("X", white, 65, 65)

        pygame.draw.rect(window, black, mu_on_bttn)
        pygame.draw.rect(window, black, mu_off_bttn)
        text("Music", black, 150, 210)
        text("On", white, 275, 210)
        text("Off", white, 430, 210)

        pygame.display.update()

def helpa():
    close_btn = pygame.Rect(50, 50, 50, 50)
    halp = True
    while halp:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousex, mousey = pygame.mouse.get_pos()
                if close_btn.collidepoint(mousex,mousey):
                    menu()
        window.fill(grn)
        pygame.draw.rect(window, black, close_btn)
        text("Help", black, x / 2 - 20, 70)
        text("X", white, 65, 65)
        text("Press A to move left", white, 100, 200)
        text("Press D to move right", white, 100, 250)
        text("Don't Crash into Cars", white, 100, 300)
        text("Go to Settings to toggle audio", white, 100, 350)
        pygame.display.update()


menu()

