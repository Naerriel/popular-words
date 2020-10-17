from src.words.frequencies import get_relative_frequencies


# book[0] - book title, book[1] - book words array
def create_chart(books):
    relative_frequencies = get_relative_frequencies(books)

    result = []

    for (i, book) in enumerate(books):
        result.append((book[0], relative_frequencies[i]))

    return result