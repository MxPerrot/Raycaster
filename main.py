"""A little raycaster project in python. using turtle graphics."""
import turtle
import math
import random
import time

# Constants
MAP = [
"111111111111111111111111",
"100000000000000000000001",
"100000000000000000000001",
"100000000000000000000001",
"100000222220000303030001",
"100000200020000000000001",
"100000200020000300030001",
"100000200020000000000001",
"100000220220000303030001",
"100000000000000000000001",
"100000000000000000000001",
"100000000000000000000001",
"100000000000000000000001",
"100000000000000000000001",
"100000000000000000000001",
"100000000000000000000001",
"144444444000000000000001",
"140400004000000000000001",
"140000504000000000000001",
"140400004000000000000001",
"140444444000000000000001",
"140000000000000000000001",
"144444444000000000000001",
"111111111111111111111111"
]

MAP_WIDTH = len(MAP[0])
MAP_HEIGHT = len(MAP)
TILE_SIDE = 16 # side length of a square, used by turtle to draw the 2d map

PIXEL_OFFSET = 200 # offset from the center of the screen
MAP_WIDTH_PIXELS = MAP_WIDTH * TILE_SIDE
MAP_HEIGHT_PIXELS = MAP_HEIGHT * TILE_SIDE

# Print some info
print("RAYCASTER")
print("Map width: ", MAP_WIDTH)
print("Map height: ", MAP_HEIGHT)
print("Tile side: ", TILE_SIDE)
print("Map width in pixels: ", MAP_WIDTH_PIXELS)
print("Map height in pixels: ", MAP_HEIGHT_PIXELS)

# Set up the screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Raycaster")

# Display the map in 2d
turtle.speed(0)
turtle.hideturtle()
turtle.penup()
for y in range(len(MAP)):
    for x in range(len(MAP[y])):
        # color the walls
        if MAP[y][x] == "0":
            continue
        elif MAP[y][x] == "1":
            turtle.color("white")
        elif MAP[y][x] == "2":
            turtle.color("red")
        elif MAP[y][x] == "3":
            turtle.color("blue")
        elif MAP[y][x] == "4":
            turtle.color("green")
        elif MAP[y][x] == "5":
            turtle.color("yellow")
        # draw the walls
        turtle.goto(
            x * TILE_SIDE - PIXEL_OFFSET,
           -y * TILE_SIDE + PIXEL_OFFSET
           )
        turtle.pendown()
        turtle.begin_fill()
        for _ in range(4):
            turtle.forward(TILE_SIDE)
            turtle.right(90)
        turtle.end_fill()
        turtle.penup()

        


# Main loop for 2d MAP
while True:
    wn.update()


