# Author: Leif Johanson
# Date: October 31, 2019
# Description: Sierpinski for A4

import turtle
import sys
import math
import random

def turtle_setup(canv_width, canv_height):
    """ Set up the canvas and a turtle for coloring pixels. Return a turtle
        object in hidden state with its pen up. The canvas has size canv_width
        by canv_height, with a coordinate system where (0,0) is in the bottom
        left corner, and automatic re-drawing of the canvas is disabled so that
        turtle.update() must be called to update the drawing.
    """
    # create a turtle to color pixels with
    t = turtle.Turtle()

    # set the screen size, coordinate system, and color mode:
    screen = t.getscreen()
    screen.setup(canv_width, canv_height)
    screen.setworldcoordinates(0, 0, canv_width, canv_height)
    turtle.colormode(255) # specify how colors are set: we'll use 0-255

    t.up() # lift the pen
    t.hideturtle() # hide the turtle triangle
    screen.tracer(0, 0) # turn off redrawing after each movement

    return t

def distance_between(p1, p2):
    """ Returns the distance between two points on a graph. Takes two points as arguments """
    x1, y1 = p1
    x2, y2 = p2
    a = ((y1 - y2)**2) + ((x1 - x2)**2)
    distance = math.sqrt(a)
    return distance
    
def midpoint(a, b):
    """ Return the midpoint between points a = (ax, ay) and b = (bx, by) """
    ax, ay = a
    bx, by = b
    mx = (ax + bx) / 2
    my = (ay + by) / 2
    return mx, my

def random_point(width, height):
    """ Creates a random point on the dimensions of the canvas. Takes width and height arguments and returns the
    value of the random coordinate in the form of a tuple. """
    rand_x = random.randint(0, width)
    rand_y = random.randint(0, height)
    rand_coord = (rand_x, rand_y)
    return rand_coord


def random_corner(width, height):
    """ Picks a random corner of the triangle with dimensions of the canvas width and height as
    arguments and returns the value in form of a tuple. """
    corner = random.choice([(width / 2, height), (0,0), (width, 0)])
    return corner

def choose_color(point):
    """ Chooses a color based on the distance of the point from the corner. Corner 1's color is red,
    corner 2's color is green, and color 3's color is blue. The function finds out what color it should be
    based on the distance from each corner, and the takes the distance and the max distance and the
    number 255 and converts it to a number between 0 and 255."""  
    width = int(sys.argv[1])
    height = int(sys.argv[2])
    c1 = (width / 2, height)
    c2 = (0, 0)
    c3 = (width, 0)
    max_distance = distance_between((width,height), (0,0))
    d_red = distance_between(c1, point)
    d_green = distance_between(c2, point)
    d_blue = distance_between(c3, point)
    turtle.colormode(255)
    # the following three functions use a math function to determine what color the dot should be based on the distance
    color_red = 255 - ((d_red/max_distance)*255)
    color_green = 255 - ((d_green/max_distance)*255)
    color_blue = 255 - ((d_blue/max_distance)*255)
    red, green, blue = int(color_red), int(color_green), int(color_blue)
    final_color = turtle.color(red, green, blue)
    return final_color

def color_pixel(point):
    """ Takes the point that will be placed and places it. This function hides the turtle, goes
    to the point where it should be placed. It then sets the dot size to 2 and then places it. """
    turtle.hideturtle()
    turtle.goto(point)
    turtle.dot(2)
    

if __name__ == "__main__":    
    # width and height are given as command line arguments:
    canv_width = int(sys.argv[1])
    canv_height = int(sys.argv[2])
    
    # Write your main program here.

    # Start by calling the turtle_setup function.
    t = turtle_setup(canv_width, canv_height)
    # Then implement the pseudocode below:

    # Chaos game - pseudocode from the assignment handout:
    # Let p be a random point in the window
    p = random_point(canv_width, canv_height)
    # loop 10000 times:
    for i in range(100000):
        c = random_corner(canv_width, canv_height)
    #     c = a random corner of the triangle
        m = midpoint(c, p)
    #     m = the midpoint between p and c
        choose_color(m)
    #     choose a color for m
        turtle.penup()
        # made an if statement so it doesnt draw the first 10
        if i > 10:
            color_pixel(m)
        turtle.pendown()
    #     color the pixel at m
        p = m
    #     p=m
        if i % 10000 == 0:
            turtle.update()
