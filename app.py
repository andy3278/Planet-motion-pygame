import pygame
import random
import math

pygame.init()

display_width = 800
display_height = 600
screen = pygame.display.set_mode((display_width, display_height))

white = (255, 255, 255)
black = (0, 0, 0)

radius1 = random.randint(10, 20)
mass1 = random.randint(100000, 1000000)

radius2 = random.randint(10, 20)
mass2 = mass1 * random.randint(90, 120) / 333000

class Planet:
    def __init__(self, x, y, mass, radius):
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
        force = (self.mass * other.mass) / (distance**2)

        # calculate direction of force
        x_direction = (other.x - self.x) / distance
        y_direction = (other.y - self.y) / distance

        # calculate acceleration f = ma
        acceleration = force / self.mass

        # calculate velocity dx and dy
        self.dx += x_direction * acceleration 
        self.dy += y_direction * acceleration 
        other.dx -= x_direction * acceleration
        other.dy -= y_direction * acceleration

    def update(self):
        self.x += self.dx
        self.y += self.dy


# create two planets 
planet1 = Planet(400, 300, mass1, radius1)
planet2 = Planet(7, 60, mass2, radius2)


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