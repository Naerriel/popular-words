from src.helpers import flat_list


def test_flatlist():
    nested_lists = [[1], [2, 3], [4, 5, 6]]
    result = flat_list(nested_lists)
    expected = [1, 2, 3, 4, 5, 6]

    assert all(a == b for a, b in zip(expected, result))