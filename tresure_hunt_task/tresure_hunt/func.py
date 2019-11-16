def find_treasure(board: list, coordinates: str = '11', path=None) -> list:

    if not path:
        path = [coordinates]

    row = int(coordinates[0])-1
    column = int(coordinates[1])-1
    value = str(board[row][column])
    if coordinates == value:
        return path

    path.append(value)
    if len(path) > len(board)**2:
        raise ValueError('This map has no treasure')
    return find_treasure(board, coordinates=value, path=path)


def make_treasure_map(l: iter, size: int = 5) -> list:
    clues_number = len(l)
    if clues_number != size**2:
        raise ValueError('You have wrong number of clues for such size')
    treasure_map = []
    count = 0
    for i in range(0, clues_number, size):
        count += size
        treasure_map.append(l[i:count])

    return treasure_map


if __name__ == '__main__':
    hints = [
        34, 21, 32, 41, 25,
        14, 42, 43, 14, 31,
        54, 45, 52, 42, 23,
        33, 15, 51, 31, 35,
        21, 52, 33, 13, 23
    ]
    treasure_map = make_treasure_map(hints)
    print(find_treasure(treasure_map))
