
def scalar_mult(val, vec):
    v = []
    for a in vec:
        v.append(a*val)
    return v

def normalise(vec):
    total = 0
    for i in range(len(vec)):
        total += vec[i]**2
    total = total **.5
    new_vec = scalar_mult(1/total, vec)
    return new_vec

def sub(v1, v2):
    if len(v1) != len(v2):
        raise
    v = []
    for i in range(len(v1)):
        v.append(v1[i]-v2[i])
    return v

def add(v1, v2):
    if len(v1) != len(v2):
        raise
    v = []
    for i in range(len(v1)):
        v.append(v1[i]+v2[i])
    return v

def dot(v1, v2):
    if len(v1) != len(v2):
        raise
    return sum([v1[i] * v2[i] for i in range(len(v1))])

def cross(v1, v2):
    return [v1[1]*v2[2] - v1[2]*v2[1], v1[2]*v2[0] - v1[0]*v2[2], v1[0]*v2[1] - v1[1]*v2[0]]
    

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
while True:
    
    screen.fill("black")
    """
    for j in range(10):
        for i in range(1, 100):
             makeline([i*1280 - count, -500, j*20-100], [i*1280 - count, 500, j*20-100])
    """
    if True:
        makecube(512, [2000, 0, 0], [math.cos(val()),math.sin(val()),0], [-math.sin(val()),math.cos(val()),0])
    count += 1
    pygame.display.flip()
