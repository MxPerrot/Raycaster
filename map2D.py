import turtle
from loadMap import load_map

def display_2d_map(MAP):
    """Display a 2d map using turtle graphics."""
    MAP_WIDTH = len(MAP[0])
    MAP_HEIGHT = len(MAP)
    TILE_SIDE = 16 # side length of a square, used by turtle to draw the 2d map

    PIXEL_OFFSET = 200 # offset from the center of the screen
    MAP_WIDTH_PIXELS = MAP_WIDTH * TILE_SIDE
    MAP_HEIGHT_PIXELS = MAP_HEIGHT * TILE_SIDE
    # Set up the screen
    wn = turtle.Screen()
    wn.bgcolor("black")
    wn.title("Raycaster")

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
    turtle.done()

if __name__ == "__main__":
    print("MAP")
    display_2d_map(
        load_map("maps/lode.txt")
    )