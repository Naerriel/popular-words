import src.words.words_count
from src.helpers import are_lists_deep_equal

words = [('I', 3), ('potatoes', 3), ('like', 1), ('much', 1)]


def test_count_occurences():
    test_words = [
        'I', 'I', 'I', 'like', 'potatoes', 'potatoes', 'potatoes', 'much'
    ]
    counts_arr = src.words.words_count.count_occurences(test_words)
    assert are_lists_deep_equal(counts_arr, words)


def test_count_words_in_book():
    assert src.words.words_count.count_words_in_book(words) == 8


def test_map_to_frequencies():
    expected = [('I', 0.375), ('potatoes', 0.375), ('like', 0.125),
                ('much', 0.125)]
    result = src.words.words_count.map_to_frequencies(words, 8)

    assert are_lists_deep_equal(result, expected)