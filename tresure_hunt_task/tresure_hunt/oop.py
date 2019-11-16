class TreasureHunt:
    def __init__(self, map_data: list, map_size: int = 5):
        self.__map_data = map_data
        self.__map_size = map_size
        self.treasure_map = self.__make_treasure_map()
        self.path = None

    def __make_treasure_map(self):
        if len(self.__map_data) != self.__map_size**2:
            raise ValueError('You have wrong map data')
        board = []
        count = 0
        for i in range(0, len(self.__map_data), self.__map_size):
            count += self.__map_size
            board.append(self.__map_data[i:count])
        return board

    def __hunt(self, start_coordinates: str) -> list:
        path = [start_coordinates]
        row = int(start_coordinates[0])-1
        column = int(start_coordinates[1])-1
        value = str(self.treasure_map[row][column])
        while start_coordinates != value:
            path.append(value)
            if len(path) > len(self.__map_data):
                raise ValueError('This map has no treasures')
            start_coordinates = value
            row = int(start_coordinates[0])-1
            column = int(start_coordinates[1])-1
            value = str(self.treasure_map[row][column])

        return path

    def find_treasure(self,  start_coordinates: str = '11') -> list:
        self.path = self.__hunt(start_coordinates)
        return self.path


if __name__ == '__main__':
    hints = [
        34, 21, 32, 41, 25,
        14, 42, 43, 14, 31,
        54, 45, 52, 42, 23,
        33, 15, 51, 31, 35,
        21, 52, 33, 13, 23
    ]
    hunt = TreasureHunt(hints)
    print(hunt.find_treasure())
