import math

import pygame

pygame.init()
WIDTH = 390
HEIGHT = 220
BORDER_COLOR = (30, 30, 30)
BALL_COLOR = (128, 65, 89)
BACKGROUND_COLOR = (255, 130, 150)
RED_COLOR = (180, 60, 60)
FIELD_COLOR = (10, 120, 80)
screen = pygame.display.set_mode((WIDTH, HEIGHT))

class Stick:
    def __init__(self, x, y):
        self.angle = 0
        self._x = x
        self._y = y
        self.radius = 40
    def update(self, mousepos):
        x = self.radius * math.cos(math.radians(self.angle)) + self._x
        y = self.radius * math.sin(math.radians(self.angle)) + self._y
        #print(x, y, self.angle)
        pygame.draw.line(screen, BORDER_COLOR, (self._x, self._y),
                         end_pos=(x, y), width=5)
        if stick.angle < 0:
            stick.angle = 360
        if self.angle > 360:
            stick.angle = 0

def calculatex_y():
    x = stick.radius * math.cos(math.radians(stick.angle)) + stick._x
    y = stick.radius * math.sin(math.radians(stick.angle)) + stick._y
    xdir = 0
    ydir = 0
    if x < xspawn: xdir = 1
    else: xdir = -1
    if y < yspawn: ydir = 1
    else: ydir = -1
    alpha = (math.atan((y * ydir) / (x * xdir)) * 180) / math.pi
    beta = 90 - alpha
    m = alpha / beta
    m1 = beta / alpha
    print(alpha, beta, m, m1)
    return m * xdir, m1 * ydir
class Ball:
    def __init__(self, x, y):
        self._x = x
        self._y = y
        pygame.draw.circle(screen, BALL_COLOR, (self._x, self._y), radius=6)
        self.dirx = 0.1
        self.diry = 0.1
    def change_dir(self, dirxx, diryy):
        self.dirx = dirxx * 0.1
        self.diry = diryy * 0.1
    def move(self):
        self._x += self.dirx
        self._y += self.diry
        if self._x >= WIDTH or self._x < 0:
            self.dirx *= -1
        if self._y >= HEIGHT or self._y < 0:
            self.diry *= -1

        pygame.draw.circle(screen, BALL_COLOR, (self._x, self._y), radius=6)


def draw_field(mousepos):
    x = xspawn
    y = yspawn
    pygame.draw.circle(screen, BALL_COLOR, (x, y), radius=6)

xspawn = 126
yspawn = 167
centerX = WIDTH/2
centerY = HEIGHT/2
running = True
ball_list = []
screen.fill(BACKGROUND_COLOR)
stick = Stick(xspawn, yspawn)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            b = Ball(xspawn, yspawn)

            b.change_dir(calculatex_y()[0], calculatex_y()[1])
            ball_list.append(b)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            stick.angle -= 10
        elif keys[pygame.K_RIGHT]:
            stick.angle += 10
    image = pygame.image.load('Screenshot 2024-02-20 182817.png')
    screen.blit(image, (-30, -30))
    if ball_list:
        for i in ball_list:
            i.move()
    stick.update(pygame.mouse.get_pos())
    draw_field(pygame.mouse.get_pos())

    pygame.display.flip()

pygame.quit()
