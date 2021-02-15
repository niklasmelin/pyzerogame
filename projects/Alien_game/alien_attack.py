import pygame
import time
import random

ship = Actor('ship', (500,400))
rocket_fire = Actor('rocket_fire', (500,400))
alien = Actor('alien', center=(100,100))

WIDTH = 1000
HEIGHT = 500

def draw():
    
    screen.clear()
    screen.blit('space_back', (0,0))
    ship.draw()
    rocket_fire.draw()
    alien.draw()
    
def move_alien(alien):   
    alien.right += 1
    if alien.left > WIDTH:
        alien.right = 0

    collide = rocket_fire.colliderect(alien)
    print (collide)

    if collide == 0:
        print ("missed")
    elif collide == 1:
        alien.image = 'pi'
        

def move_rocket(ship):
    if keyboard.left:
        ship.x -= 1
        rocket_fire.x -=1
    elif keyboard.right:
        ship.x += 1
        rocket_fire.x +=1
    elif keyboard.space:
        animate(rocket_fire, pos =(0, 0))
        screen.clear()
    
def update():
    move_alien(alien)
    move_rocket(ship)
    draw()

    
        
   
