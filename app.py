import pygame
import random
import math

pygame.init()

display_width = 800
display_height = 600
screen = pygame.display.set_mode((display_width, display_height))

white = (255, 255, 255)
black = (0, 0, 0)

# gravitational constatn
G = 6.67408 * 10**-11


radius1 = random.randint(10, 20)
mass1 = random.randint(10**9, 10**12)

radius2 = random.randint(10, 20) / 10
mass2 = mass1 * random.randint(90, 120) / 333000

class Planet:
    def __init__(self, x, y, mass, radius, init_dx=0, init_dy=0):
        self.x = x
        self.y = y
        self.mass = mass
        self.radius = radius
        self.dx = 0
        self.dy = 0
    def draw(self):
        pygame.draw.circle(screen, white, (self.x, self.y), self.radius)
    
    def force(self, other):
        # calculate distance between two planets
        distance  = math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

        # calculate force
        force = (G * self.mass * other.mass) / (distance**2)
        angle = math.atan2(other.y - self.y, other.x - self.x)

        acceleration = force / self.mass
        # calculate acceleration
        x_acceleration = acceleration * math.cos(angle)
        y_acceleration = acceleration * math.sin(angle)

        # calculate velocity dx and dy
        self.dx += x_acceleration
        self.dy += y_acceleration
        other.dx -= x_acceleration
        other.dy -= y_acceleration

    def update(self):
        self.x += self.dx
        self.y += self.dy


# create two planets 
planet1 = Planet(400, 300, mass1, radius1)
planet2 = Planet(7, 60, mass2, radius2, 200 , 200)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    planet1.draw()
    planet2.draw()

    # calculate force
    planet1.force(planet2)
    planet2.force(planet1)

    # update planet position
    planet1.update()
    planet2.update()

    pygame.display.update()

pygame.quit()