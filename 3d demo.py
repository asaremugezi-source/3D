from vectormath import *
import pygame
def f(p, v):
    if len(p)-1 != len(v):
        raise
    x = 0
    for i in range(len(p)-1):
        x += p[i]*v[i]
    s = p[-1]/x
    return [a*s for a in v]

def makeline(a, b, width = 512, height = 512, depth = 1280):
    try:
        a = f([1,0,0,depth],a)
        b = f([1,0,0,depth],b)
        pygame.draw.line(screen, "white", (width//2+a[1],height//2+a[2]), (width//2+b[1],height//2+b[2]))
    except ZeroDivisionError:
        return

def makecube(s, c, v1, v2):
    v1 = normalise(v1)
    v2 = normalise(sub(v2, scalar_mult(dot(v1, v2), v1)))
    v3 = normalise(cross(v1, v2))
    v = [v1,v2,v3]
    def find_corner(n):
        c = corner
        for k in range(3):
            if (1 << k) & n:
                c = add(c, scalar_mult(s,v[k]))
        return c
    corner = c
    for vi in v:
        corner = sub(corner, scalar_mult(s/2, vi))
    for i in range(8):
        for j in range(3):
            val = (1 << j) ^ i
            if val > i:
                makeline(find_corner(i), find_corner(val))
    
pygame.init()
screen = pygame.display.set_mode((512,512))
count = 0
val = lambda :count/10000
import math
while __name__ == "__main__":
    screen.fill("black")
    makecube(512, [2000, 0, 0], [math.cos(val()),math.sin(val()),0], [-math.sin(val()),math.cos(val()),0])
    count += 1
    pygame.display.flip()
