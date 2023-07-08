from canvas import Canvas
from shapes import Rectangle, Square

# get canvas width and height for user
canvas_width = int(input("Enter canvas width: "))
canvas_height = int(input("Enter canvas height: "))

# Make a dictionary of color codes and prompt for color
colors = {"white": (255, 255, 255), "black": (0, 0, 0)}
canvas_color = input("Enter canvas color (white or black): ")

# Create a canvas with user data
canvas = Canvas(height=canvas_height, width=canvas_width, color=colors[canvas_color.lower()])

while True:
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

    # Break the loop if user entered 'quit'
    if shape_type == 'quit' or shape_type == 'Quit':
        break

canvas.make('canvas.png')