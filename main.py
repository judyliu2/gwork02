from display import *
from draw import *

s = new_screen()
c = [ 80, 228, 75 ]


draw_line(200,350, XRES/2+10, YRES/2, s, c)
draw_line(XRES/2+10, YRES/2, XRES/2+100, YRES/2+100,s,c)
draw_line(XRES/2+100, YRES/2+100,XRES/2+200, YRES/2,s,c)
draw_line(XRES/2+200, YRES/2, 350, 300,s,c)
draw_line(350, 300,XRES/2, YRES/2 -50,s,c)
draw_line(XRES/2, YRES/2 -50, 175, 300, s,c)
draw_line(175, 300, 120, YRES-210, s,c)
draw_line(120, YRES-210,150, 320, s,c)
draw_line(150, 320,100,340, s,c)
draw_line(100,340,100,360, s,c)
draw_line(100,360,150,380, s,c)
draw_line(150,380,200,350, s,c)
draw_line(20,0,475,0, s,c)
draw_line(0,20,0,475, s,c)

draw_line(25,10,40,475, s,c)
draw_line(20,475,40,200, s,c)
draw_line(0,0,200,200, s,c)
draw_line(0,200,200,0, s,c)

c= [218, 69, 104]
draw_line(100,320,140,322,s,c)
draw_line(100,320,110,310,s,c)
draw_line(110,310,100,300,s,c)
draw_line(100,300,145,318,s,c)

display(s)
save_extension(s, 'img.png')


