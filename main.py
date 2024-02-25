"""A little raycaster project in python. using turtle graphics."""
from map2D import display_2d_map
from loadMap import load_map

def main():
    """Main function."""
    display_2d_map(
        load_map("maps/lode.txt")
    )

main()