# ================================================
# COLOUR LOOP SPHERE ARTWORK
# ================================================
# Topics:
# The Turtle Library | Setting Up the Canvas
# Moving the Turtle | Pen Control
# Drawing Shapes with Fill

import turtle

# ------------------------------------------------
# PART 1 — SET UP THE CANVAS
# ------------------------------------------------

screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Colour Loop Sphere")

# ------------------------------------------------
# PART 2 — CREATE THE TURTLE
# ------------------------------------------------

art = turtle.Turtle()
art.speed("fastest")
art.hideturtle()
art.pensize(2)

# ------------------------------------------------
# PART 3 — DRAW A GEOMETRIC ELEMENT
# ------------------------------------------------

def draw_loop_circle(radius, colour):
    "Draws an unfilled outline circle using the given color."
    art.color(colour)
    art.circle(radius)

# ------------------------------------------------
# PART 4 — CREATE THE COLOUR LOOP ARTWORK
# ------------------------------------------------

# Diverse vibrant color palette matching the overlapping threads in your image
colours = [
    "#00A8E8", "#DE3163", "#FFBF00", "#4CBB17", 
    "#900C3F", "#FF5733", "#8E44AD", "#1ABC9C"
]

# Loop 72 times (5-degree increments) to create the ultra-dense woven look
for i in range(72):
    draw_loop_circle(150, colours[i % len(colours)])
    art.right(5)

# ------------------------------------------------
# PART 5 — KEEP THE WINDOW OPEN
# ------------------------------------------------

turtle.done()
