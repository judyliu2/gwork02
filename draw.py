
from display import *

def draw_line( x0, y0, x1, y1, screen, color ):
    #check octant
    m = (y1 - y0)/(x1 - x0)
    if (m > 0 and m < 1): #quadrants 1 and 5
        A = x0+1
        B = y0 + 0.5
        d = 2A + B
        while (x0 <= x1):
            plot(screen,color, x0, y0)
            if( d > 0):
                y++
                d+=2B
            x++
            d+= 2A
            
    if (m > 1): #quadrants 2 and 6
        A = x0 + .5
        B = y0 + 1
        d = A + 2B
        while (y0<=y1):
            plot(screen,color, x0, y0)
            if (d<0):
                x++
                d+=2A
            y++
            d+=2B
            #quadrants 3 and 7
    if (m < 0 and m > -1):
        A = x0 + 0.5
        B = y - 1
        d = 2A + B
        while (y0 >= y1):
            plot(screen,color, x0, y0)
            if (d<0):
                x++
                d-=2A
            y++
            d-=B
            #quadrants 4 and 8
    if( m < -1):
        A = x0 + 1
        B = y - .5
        d = A + 2B
        while(x0 >= x1):
            plot(screen,color, x0, y0)
            if (d>0):
                y++
                d-=2A
            x++
            d-=2B
pass
