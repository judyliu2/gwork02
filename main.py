from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]

display(screen)
save_extension(screen, 'img.png')

drawline(XRES-1, YRES-1, 0,0, screen,color)
