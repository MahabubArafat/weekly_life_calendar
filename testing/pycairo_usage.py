"""
pycairo is needed for this project and its installed on fun_venv in area
https://pycairo.readthedocs.io/en/latest/tutorial.html
https://github.com/pygobject/pycairo/blob/master/examples/pycairo_examples.ipynb
"""
import cairo
import math

WIDTH,HEIGHT=256,256

surface=cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
context=cairo.Context(surface)

context.scale(WIDTH, HEIGHT) #canvas making

pat = cairo.LinearGradient(0.0, 0.0, 0.0, 1.0)
pat.add_color_stop_rgba(1, 0.7, 0, 0, 0.5)  # First stop, 50% opacity
pat.add_color_stop_rgba(0, 0.9, 0.7, 0.2, 1)  # Last stop, 100% opacity

context.rectangle(0, 0, 1, 1)
context.set_source(pat)
context.fill()

context.translate(0.1, 0.1) #mane koi theke drawing start

context.move_to(0, 0)

# context.arc(0.2, 0.1, 0.1, -math.pi / 2, 0)
# Arc(cx, cy, radius, start_angle, stop_angle)

# context.line_to(0.5, 0.1)  # Line to (x,y)

# Curve(x1, y1, x2, y2, x3, y3)
# context.curve_to(0.5, 0.2, 0.5, 0.4, 0.2, 0.8)
# context.close_path()


#making a square
context.line_to(0.5, 0)
context.line_to(0.5, 0.5)
context.line_to(0, 0.5)
context.close_path()
context.line_to(0.5, 0.5)
context.move_to(0.5, 0)
context.line_to(0, 0.5)
context.arc(0.5, 0.5, 0.25, 0.25, 0)



context.set_source_rgb(0.0, 1.0, 0.16)  # Solid color
context.set_line_width(0.02)
context.stroke()





surface.write_to_png("example.png")


