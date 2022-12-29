import pygame
import random


class Particle:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.xvel = 0
        self.yvel = 0
        self.mass = 1
        self.age = 0


    def applyForce(self, x, y):
        self.xvel = self.xvel + (x / self.mass)
        self.yvel = self.yvel + (y / self.mass)

    def update(self, particles):
        self.age += 1
        self.applyForce(0, 0.001)
        self.applyForce(self.xvel * -0.001, self.yvel * -0.001)

        # collision with walls
        if self.x > SCREEN_W:
            self.x = SCREEN_W
            self.xvel = self.xvel * -1
        if self.x < 0:
            self.x = 0
            self.xvel = self.xvel * -1

        if self.y > SCREEN_H:
            self.y = SCREEN_H
            self.yvel = self.yvel * -1
        if self.y < 0:
            self.y = 0
            self.yvel = self.yvel * -1

        # collision with other particles
        # for particle in particles:
        #     if self.x == particle.x and self.y == particle.y:
        #         continue

        #     myradiusSquared = 100

        #     distanceSquared = pow(self.x - particle.x, 2) + pow(self.y - particle.y, 2)

        #     if distanceSquared < myradiusSquared:
        #         self.applyForce((self.x - particle.x) * 0.005, (self.y - particle.y) * 0.005)
        #         particle.applyForce((particle.x - self.x) * 0.005, (particle.y - self.y) * 0.005)


        self.x = self.x + self.xvel
        self.y = self.y + self.yvel

particles = []

WHITE = pygame.Color(255, 255, 255)

SCREEN_W = 640
SCREEN_H = 480

pygame.init()
pygame.font.init()
pygame.image.get_extended()

screen_rect = pygame.Rect(0, 0, SCREEN_W, SCREEN_H)
screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))

run = True

while run:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if len(particles) < 1000:
        p = Particle(300, 200)
        xforce = random.random() * pow(-1, random.randint(0, 1))
        yforce = random.random() * pow(-1, random.randint(0, 1))
        p.applyForce(xforce, yforce)
        particles.append(p)
    
    for particle in particles:
        if particle.age > 1000:
            particle.age = 0
            particle.x = 300
            particle.y = 200
            particle.xvel = 0
            particle.yvel = 0
            xforce = random.random() * pow(-1, random.randint(0, 1))
            yforce = random.random() * pow(-1, random.randint(0, 1))
            particle.applyForce(xforce, yforce)
        particle.update(particles)
        lValue = int(255 * (particle.age) / 1000.0)
        # a = int(255 * (1000 - particle.age) / 1000.0)
        color = pygame.Color(255, lValue, 0)
        pygame.draw.circle(screen, color, (particle.x, particle.y), 5)

    pygame.display.flip()
