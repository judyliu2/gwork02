from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]

display(screen)
save_extension(screen, 'img.png')

plot(screen, color, XRES/2, YRES/2);
