import src.words.main
from src.helpers import flat_list

books = [['First', ['word', 'word', 'word', 'secWord', 'seventhWord']],
         [
             'Second',
             ['secWord', 'secWord', 'thirdWord', 'thirdWord', 'thirdWord']
         ]]

words = [[('one', 2), ('two', 3), ('three', 5)],
         [('one', 2), ('dos', 6), ('tres', 2)]]


def test_getting_relative_frequencies():
    result = src.words.main.get_relative_frequencies(books)
    expected = [[('word', 2.0), ('secWord', 0.6666666666666667),
                 ('seventhWord', 2.0)],
                [('thirdWord', 2.0), ('secWord', 1.3333333333333335)]]

    assert all(a == b for a, b in zip(flat_list(result), flat_list(expected)))


def test_getting_frequencies_per_total():
    result = src.words.main.get_total_frequencies_of_words(words)
    expected = {
        'one': 0.2,
        'two': 0.15,
        'three': 0.25,
        'dos': 0.3,
        'tres': 0.1
    }
    print(result)

    assert all(result[key] == expected[key] for key in result)


def test_getting_frequencies_per_books():
    result = src.words.main.get_local_frequencies_per_books(words)

    expected = [
        [('one', 0.2), ('two', 0.3), ('three', 0.5)],
        [('one', 0.2), ('dos', 0.6), ('tres', 0.2)],
    ]

    assert all(a == b for a, b in zip(flat_list(result), flat_list(expected)))


def test_getting_relative_frequencies_per_books():
    result = src.words.main.get_relative_frequencies_per_books([
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

    assert all(a == b for a, b in zip(flat_list(expected), flat_list(result)))