import src.words.frequencies
from src.helpers import flat_list, are_lists_deep_equal, are_dictionaires_equal

books = [[
    'First', ['word', 'word', 'word', 'secWord', 'thirdWord', 'seventhWord']
],
         [
             'Second',
             [
                 'word', 'secWord', 'secWord', 'thirdWord', 'thirdWord',
                 'thirdWord', 'milionthWord'
             ]
         ]]

words = [[('one', 2), ('two', 3), ('three', 5)],
         [('one', 2), ('dos', 6), ('tres', 2)]]


def test_getting_relative_frequencies():
    result = src.words.frequencies.get_relative_frequencies(books)
    expected = [[('word', 1.9499999999999997), ('secWord', 0.8666666666666667),
                 ('thirdWord', 0.65)],
                [('thirdWord', 1.625), ('secWord', 1.4444444444444442),
                 ('word', 0.5416666666666666)]]

    assert are_lists_deep_equal(expected, result)

    result_uniques = src.words.frequencies.get_relative_frequencies(
        books, False)
    expected_uniques = [[('seventhWord', 2.1666666666666665), ('word', 1.625),
                         ('secWord', 0.7222222222222221),
                         ('thirdWord', 0.5416666666666666)],
                        [('milionthWord', 1.857142857142857),
                         ('thirdWord', 1.3928571428571428),
                         ('secWord', 1.238095238095238),
                         ('word', 0.46428571428571425)]]
    assert are_lists_deep_equal(expected_uniques, result_uniques)


def test_getting_frequencies_per_total():
    result = src.words.frequencies.get_total_frequencies_of_words(words)
    expected = {
        'one': 0.2,
        'two': 0.15,
        'three': 0.25,
        'dos': 0.3,
        'tres': 0.1
    }

    assert are_dictionaires_equal(result, expected)


def test_getting_frequencies_per_books():
    result = src.words.frequencies.get_local_frequencies_per_books(words)

    expected = [
        [('one', 0.2), ('two', 0.3), ('three', 0.5)],
        [('one', 0.2), ('dos', 0.6), ('tres', 0.2)],
    ]

    assert are_lists_deep_equal(expected, result)


def test_getting_relative_frequencies_per_books():
    result = src.words.frequencies.get_relative_frequencies_per_books(
        [
            [('one', 0.2), ('two', 0.3), ('three', 0.5)],
            [('one', 0.2), ('dos', 0.6), ('tres', 0.2)],
        ], {
            'one': 0.2,
            'two': 0.15,
            'three': 0.25,
            'dos': 0.3,
            'tres': 0.1
        })

    expected = [
        [('one', 1), ('two', 2), ('three', 2)],
        [('one', 1), ('dos', 2), ('tres', 2)],
    ]

    assert are_lists_deep_equal(expected, result)


def test_getting_sorted_frequencies():
    relative_frequencies_per_books = [
        [('one', 1), ('two', 2), ('three', 2)],
        [('dos', 2), ('one', 1), ('tres', 2)],
    ]
    result = src.words.frequencies.get_sorted_frequencies(
        relative_frequencies_per_books)

    expected = [
        [('two', 2), ('three', 2), ('one', 1)],
        [('dos', 2), ('tres', 2), ('one', 1)],
    ]
    print(result)

    assert are_lists_deep_equal(result, expected)


def test_filtering_out_words_in_single_book():
    test_words = [[('one', 2), ('two', 3), ('three', 5), ('four', 6),
                   ('five', 4)],
                  [('one', 2), ('two', 6), ('three', 2), ('four', 9),
                   ('six', 1)]]
    result = src.words.frequencies.filter_out_words_in_single_book(test_words)
    expected = [[('one', 2), ('two', 3), ('three', 5), ('four', 6)],
                [('one', 2), ('two', 6), ('three', 2), ('four', 9)]]
    print(result)

    assert are_lists_deep_equal(result, expected)
