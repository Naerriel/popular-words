from src.words.words_count import count_occurences, count_words_in_book, map_to_frequencies
from src.helpers import flat_list


# book[0] - book title, book[1] - book words array
def create_chart(books):
    relative_frequencies = get_relative_frequencies(books)
    print(relative_frequencies)


def get_local_frequencies_per_books(words_occurences_per_books):
    words_per_books = [
        count_words_in_book(words_occurences)
        for words_occurences in words_occurences_per_books
    ]
    return [
        map_to_frequencies(words_occurences, words_per_books[i])
        for (i, words_occurences) in enumerate(words_occurences_per_books)
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


def get_relative_frequencies(books):
    words_occurences_per_books = [count_occurences(book[1]) for book in books]

    total_frequencies = get_total_frequencies_of_words(
        words_occurences_per_books)

    local_frequencies_per_books = get_local_frequencies_per_books(
        words_occurences_per_books)
    return get_relative_frequencies_per_books(local_frequencies_per_books,
                                              total_frequencies)
