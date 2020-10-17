from src.helpers import flat_list, are_lists_deep_equal, are_dictionaires_equal


def test_flatlist():
    nested_lists = [[1], [2, 3], [4, 5, 6, [7, 8]]]
    result = flat_list(nested_lists)
    expected = [1, 2, 3, 4, 5, 6, 7, 8]

    assert all(a == b for a, b in zip(expected, result))


def test_are_lists_deep_equal():
    list_a = [[12], [3]]
    list_b = [[12], [3]]
    assert are_lists_deep_equal(list_a, list_b)
    assert not are_lists_deep_equal([1, 2, 3], [1, 2])


def test_are_dictionaires_equal():
    dict_a = {
        'a': 13,
        'b': 15,
    }
    dict_b = {
        'a': 13,
        'b': 15,
    }
    dict_c = {
        'a': 13,
    }

    assert are_dictionaires_equal(dict_a, dict_b)
    assert not are_dictionaires_equal(dict_a, dict_c)