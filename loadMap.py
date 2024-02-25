def load_map(file_name):
    """Loads a map from a text file."""
    finalList = []
    with open(file_name, "r") as f:
        lines = f.readlines()

    for line in lines:
        finalList.extend([int(x) for x in line.strip()])

    mapX = len(lines[0].strip())
    mapY = len(lines)
        
        
    return finalList, mapX, mapY
        
    
if __name__ == "__main__":
    print(load_map("maps/square_20.txt"))