import pygame
import pygame.camera
from pygame.locals import *
import cv2
#import os

pygame.init()
pygame.camera.init()
cascadePath = 'haarcascade_frontalface_default.xml'

faceCascade = cv2.CascadeClassifier(cascadePath)

cap = cv2.VideoCapture(0)

class Ball:
    RADIUS = 10
    speed = 200
    DISTANTION_COLLIDER = 5

    def __init__(self, coords: tuple[int, int]):
        self._x, self._y = coords
        self.x_val = -1
        self.y_val = -1

    def go(self):
        self._x += self.speed / FPS * self.x_val
        self._y += self.speed / FPS * self.y_val
        if (self._x - self.RADIUS) < 3 or (self._x + self.RADIUS) > WIDTH - 3:
            self.x_val *= -1
        elif (self._y - self.RADIUS) < 3 or (self._y + self.RADIUS) > HEIGHT - 3:
            self.y_val *= -1
        # for i in balls:
        #     if ((self._x - self.RADIUS > (i._x - i.RADIUS)) and (
        #             self._x - self.RADIUS < (i._x - i.RADIUS) + self.DISTANTION_COLLIDER)) or (
        #             (self._x + self.RADIUS > (i._x + i.RADIUS)) and (
        #             self._x + self.RADIUS < (i._x + i.RADIUS) - self.DISTANTION_COLLIDER)):
        #         self.x_val *= -1
        #         i.x_val *= -1
        #     elif ((self._y - self.RADIUS > (i._y - i.RADIUS)) and (
        #             self._y - self.RADIUS < (i._y - i.RADIUS) + self.DISTANTION_COLLIDER)) or (
        #             (self._y + self.RADIUS > (i._y + i.RADIUS)) and (
        #             self._y + self.RADIUS < (i._y + i.RADIUS) - self.DISTANTION_COLLIDER)):
        #         self.y_val *= -1
        #         i.y_val *= -1

    def test_of_cube(self, x_cube, y_cube, x2_cube, y2_cube):
        if (self._x - self.RADIUS) < x_cube or (self._x + self.RADIUS) > x2_cube:
            self.x_val *= -1
        if (self._y - self.RADIUS) < y_cube or (self._y + self.RADIUS) > y2_cube:
            self.y_val *= -1

    def draw(self, screen: pygame.Surface):
        pygame.draw.circle(screen, (255, 255, 255), (self._x, self._y), self.RADIUS)
class Capture:
    def __init__(self):

        self.sh = pygame.Surface(size, 0, screen)
        self.coof = 10
    def get_and_flip(self):
        ret, frame = cap.read()
        rgb = cv2.rotate(frame, cv2.ROTATE_90_COUNTERCLOCKWISE)
        rgb = cv2.cvtColor(rgb, cv2.COLOR_BGR2RGB)

        self.sh = pygame.surfarray.make_surface(rgb)
        screen.blit(self.sh, (0, 0))

        gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
        faces = faceCascade.detectMultiScale(gray, 2, 2)
        for (x, y, w, h) in faces:
            x = 640 - x
            w = w - self.coof
            for i in balls:
                i.test_of_cube(x - w, y, x - w, y + w)
            pygame.draw.polygon(screen, (255, 255, 255), ((x - w, y), (x - w, y + w), (x, y + w), (x, y)), 1)
        pygame.display.flip()

work = True
if __name__ == '__main__':
    balls: list[Ball] = []
    BACKGROUND = pygame.color.Color(35, 35, 35)
    FPS = 60
    WIDTH, HEIGHT, size = 640, 480, (640, 480)
    screen = pygame.display.set_mode(size, 0)
    cm = Capture()

    while work:
        cm.get_and_flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                work = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                balls.append(Ball(event.pos))
        for i in balls:
            i.go()
            i.draw(screen)
        pygame.display.flip()
pygame.quit()
quit()
