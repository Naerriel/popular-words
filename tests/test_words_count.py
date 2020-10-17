import src.words.words_count

words = [('I', 3), ('potatoes', 3), ('like', 1), ('much', 1)]


def test_count_occurences():
    test_words = [
        'I', 'I', 'I', 'like', 'potatoes', 'potatoes', 'potatoes', 'much'
    ]
    counts_arr = src.words.words_count.count_occurences(test_words)

    assert len(counts_arr) == len(words)
    assert all(
        [a[0] == b[0] and a[1] == b[1] for a, b in zip(counts_arr, words)])


def test_count_words_in_book():
    assert src.words.words_count.count_words_in_book(words) == 8


def test_map_to_frequencies():
    expected = [('I', 0.375), ('potatoes', 0.375), ('like', 0.125),
                ('much', 0.125)]
    result = src.words.words_count.map_to_frequencies(words, 8)
    print(result)

    assert len(result) == len(words)
    assert all(a == b for a, b in zip(result, expected))