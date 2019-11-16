import pytest

from tresure_hunt.func import make_treasure_map, find_treasure


def test_right_map():
    hints = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert [[1, 2, 3], [4, 5, 6], [7, 8, 9]] == make_treasure_map(hints, 3)


def test_wrong_size_map():
    hints = [1, 2, 3, 4, 5, 6, 7, 8]
    with pytest.raises(ValueError):
        make_treasure_map(hints, 3)


def test_find_treasure():
    treasure_map = [[34, 21, 32, 41, 25],
                    [14, 42, 43, 14, 31],
                    [54, 45, 52, 42, 23],
                    [33, 15, 51, 31, 35],
                    [21, 52, 33, 13, 23]]

    assert ['11', '34', '42', '15', '25',
            '31', '54', '13', '32', '45',
            '35', '23', '43', '51', '21',
            '14', '41', '33', '52'] == find_treasure(treasure_map)


def test_no_treasure():
    treasure_map = [[34, 21, 32, 41, 25],
                    [14, 42, 43, 14, 31],
                    [54, 45, 52, 42, 23],
                    [33, 15, 51, 31, 35],
                    [21, 13, 33, 13, 23]]

    with pytest.raises(ValueError):
        find_treasure(treasure_map)


def test_another_start():
    treasure_map = [[34, 21, 32, 41, 25],
                    [14, 42, 43, 14, 31],
                    [54, 45, 52, 42, 23],
                    [33, 15, 51, 31, 35],
                    [21, 52, 33, 13, 23]]

    assert ['31', '54', '13', '32',
            '45', '35', '23', '43',
            '51', '21', '14', '41',
            '33', '52'] == find_treasure(treasure_map, coordinates='31')
