import pgzero

WIDTH = 300
HEIGHT = 300

alien = Actor('alien')
alien.pos = 100, 56


def draw():
    screen.clear()
    alien.draw()
