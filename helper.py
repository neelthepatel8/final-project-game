def generate_puzzle_data(f):
    """Generates the dictionary for the puzzle

    Args:
        f (str): path of the puz file

    Returns:
        dict: Dictionary with data of puzzle
    """
    data = {}
    data["images"] = {}
    with open(f, mode="r") as file:
        for index, line in enumerate(file):
            key = line.split(":")[0]
            value = line.split(":")[1].strip()
            if index >= 4:
                data["images"][key] = value
                continue
            data[key] = value
    return data