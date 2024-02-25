def load_map(file_name):
    """Load a map from a file."""
    with open(file_name, "r") as f:
        return [line.strip() for line in f.readlines()]
    
if __name__ == "__main__":
    print(load_map("maps/square_5.txt"))