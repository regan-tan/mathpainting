import numpy as np
from PIL import Image

class Canvas:
    """Object where all shapes will be drawn in"""
    
    def __init__(self, height, width, color):
        self.color = color
        self.height = height
        self.width = width

        # Create a 3d numpy array of zeros
        self.data = np.zeros((self.height, self.width, 3), dtype=np.uint8)
        # Change [0, 0, 0] with user given values for color
        self.data[:] = self.color

    def make(self, imagepath):
        """Converts the current array into an image file"""
        img = Image.fromarray(self.data, 'RGB')
        img.save(imagepath)


class Rectangle:
    """A rectangle shape that can be drawn on a Canvas object"""

    def __init__(self, x, y, height, width, color):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.color = color
    
    def draw(self, canvas):
        """Draws itself into the canvas"""
        # Changes a slice of the array with new values
        canvas.data[self.x: self.x + self.height, self.y: self.y + self.width] = self.color



class Square:
    """A square shape that can be drawn on a Canvas object"""

    def __init__(self, x, y, side, color):
        self.x = x
        self.y = y
        self.side = side
        self.color = color
    
    def draw(self, canvas):
        """Draws itself into the canvas"""
        # Changes a slice of the array with new values
        canvas.data[self.x: self.x + self.side, self.y: self.y + self.side] = self.color



canvas = Canvas(height=20, width=30, color=[255, 255, 255])
r1 = Rectangle(x=1, y=6, height=7, width=10, color=(100, 200, 125))
r1.draw(canvas)
s1 = Square(x=1,y=3, side=3, color=(0, 100, 222))
s1.draw(canvas)
canvas.make('canvas.png')

from canvas import Canvas
from shapes import Rectangle, Square

# get canvas width and height for user
canvas_width = int(input("Enter canvas width: "))
canvas_height = int(input("Enter canvas height: "))

# Make a dictionary of color codes and prompt for color
colors = {"white": (255, 255, 255), "black": (0, 0, 0)}
canvas_color = input("Enter canvas color (white or black): ")

# Create a canvas with user data
canvas = Canvas(height=canvas_height, width=canvas_width, color=colors[canvas_color])

while true:
    shape_type = input("What do you like to draw? Enter quit to quit. ")
    # Ask for rectangle data and create rectangle if user entered 'rectangle'
    if shape_type.lower() == 'rectangle':
        rec_x = int(input("Enter x of rectangle: "))
        rec_y = int(input("Enter y of rectangle: "))
        rec_width = int(input("Enter width of rectangle: "))
        rec_height = int(input("Enter height of rectangle: "))
        red = int(input("How much red should the rectangle have? "))
        green = int(input("How much green? "))
        blue = int(input("How much blue? "))

        # Create the rectangle
        r1 = Rectangle(x=rec_x, y=rec_y, height=rec_height, width=rec_width, color=(red, green, blue))
        r1.draw(canvas)

    # Ask for square data and create square if user entered 'square'
    if shape_type.lower() == 'square':
        sqr_x = int(input("Enter x of square: "))
        sqr_y = int(input("Enter y of square: "))
        sqr_side = int(input("Enter the length of a side of the square: "))
        red = int(input("How much red should the square have? "))
        green = int(input("How much green? "))
        blue = int(input("How much blue? "))

        # Create the square
        r1 = Square(x=sqr_x, y=sqr_y, side=sqr_side, color=(red, green, blue))
        r1.draw(canvas)