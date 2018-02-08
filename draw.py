
from display import *

def draw_line( x0, y0, x1, y1, screen, color ):
    x1 = x0;
    x1 = y0;
    #check octant
    m = (y1 - y0)/(x1 - x0)
    if (m > and m < 1):
        A = x0+1
        B = y0 + 0.5
        d = 2A + B
        while (x0 <= x1):
            plot(screen,color, x0, y0)
            if( d > 0):
                y++
                d+=2
            x++
            d+= 2A
    if (m > 1 ){
            
    }
pass
