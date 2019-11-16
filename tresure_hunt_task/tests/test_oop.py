import pytest

from tresure_hunt.oop import TreasureHunt


def test_right_map():
    hints = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    treasure_hunt = TreasureHunt(hints, map_size=3)
    assert [[1, 2, 3], [4, 5, 6], [7, 8, 9]] == treasure_hunt.treasure_map


def test_wrong_size_map():
    hints = [1, 2, 3, 4, 5, 6, 7, 8]
    with pytest.raises(ValueError):
        TreasureHunt(hints)


def test_find_treasure():
    hints = [34, 21, 32, 41, 25,
             14, 42, 43, 14, 31,
             54, 45, 52, 42, 23,
             33, 15, 51, 31, 35,
             21, 52, 33, 13, 23]
    treasure_hunt = TreasureHunt(hints)

    assert ['11', '34', '42', '15', '25',
            '31', '54', '13', '32', '45',
            '35', '23', '43', '51', '21',
            '14', '41', '33', '52'] == treasure_hunt.find_treasure()


def test_no_treasure():
    hints = [34, 21, 32, 41, 25,
             14, 42, 43, 14, 31,
             54, 45, 52, 42, 23,
             33, 15, 51, 31, 35,
             21, 13, 33, 13, 23]

    with pytest.raises(ValueError):
        treasure_hunt = TreasureHunt(hints)
        treasure_hunt.find_treasure()


def test_another_start():
    hints = [34, 21, 32, 41, 25,
             14, 42, 43, 14, 31,
             54, 45, 52, 42, 23,
             33, 15, 51, 31, 35,
             21, 52, 33, 13, 23]
    treasure_hunt = TreasureHunt(hints)

    assert ['31', '54', '13', '32',
            '45', '35', '23', '43',
            '51', '21', '14', '41',
            '33', '52'] == treasure_hunt.find_treasure(start_coordinates='31')
