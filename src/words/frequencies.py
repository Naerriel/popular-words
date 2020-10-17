from src.words.words_count import count_occurences, count_words_in_book, map_to_frequencies
from src.helpers import flat_list


def get_local_frequencies_per_books(words_occurences_per_books):
    words_per_books = [
        count_words_in_book(words_occurences)
        for words_occurences in words_occurences_per_books
    ]
    return [
        map_to_frequencies(words_occurences, words_per_books[i])
        for (i, words_occurences) in enumerate(words_occurences_per_books)
    ]


def filter_out_words_in_single_book(words_occurences_per_books):
    all_books_words_count = {}

    for words_occurences in words_occurences_per_books:
        for word in words_occurences:
            if word[0] in all_books_words_count:
                all_books_words_count[word[0]] += word[1]
            else:
                all_books_words_count[word[0]] = word[1]

    words_to_skip = {}

    for words_occurences in words_occurences_per_books:
        count_per_book = {}
        for word in words_occurences:
            if word[0] in count_per_book:
                count_per_book[word[0]] += word[1]
            else:
                count_per_book[word[0]] = word[1]

        for wordTxt in count_per_book:
            isWordInSingleBook = count_per_book[
                wordTxt] == all_books_words_count[wordTxt]
            if isWordInSingleBook:
                words_to_skip[wordTxt] = True

    def get_filtered_words_occurences(words_occurences):
        result = []
        for word in words_occurences:
            if not word[0] in words_to_skip:
                result.append(word)
        return result

    return [
        get_filtered_words_occurences(words_occurences)
        for words_occurences in words_occurences_per_books
    ]


def get_relative_frequencies_per_books(local_frequencies_per_books,
                                       total_frequencies):
    def get_value(word):
        return (word[0], word[1] / total_frequencies[word[0]])

    return [[get_value(word) for word in local_frequencies]
            for local_frequencies in local_frequencies_per_books]


def get_total_frequencies_of_words(words_occurences_per_books):
    total_words = 0
    counts = {}

    for word in flat_list(words_occurences_per_books):
        total_words += word[1]
        if word[0] in counts:
            counts[word[0]] += word[1]
        else:
            counts[word[0]] = word[1]

    for word in counts:
        counts[word] = counts[word] / total_words

    return counts


def get_relative_frequencies(books, filter_uniques=True):
    words_occurences_per_books = [count_occurences(book[1]) for book in books]

    total_frequencies = get_total_frequencies_of_words(
        words_occurences_per_books)

    local_frequencies_per_books = []
    if filter_uniques:
        local_frequencies_per_books = get_local_frequencies_per_books(
            filter_out_words_in_single_book(words_occurences_per_books))
    else:
        local_frequencies_per_books = get_local_frequencies_per_books(
            words_occurences_per_books)

    return get_sorted_frequencies(
        get_relative_frequencies_per_books(local_frequencies_per_books,
                                           total_frequencies))


def get_sorted_frequencies(relative_frequencies_per_books):
    return [
        sorted(relative_frequencies, key=lambda x: x[1], reverse=True)[:20]
        for relative_frequencies in relative_frequencies_per_books
    ]
