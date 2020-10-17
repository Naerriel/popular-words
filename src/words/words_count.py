#!/usr/bin/env python3


def count_occurences(words):
    counts = {}
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    counts_arr = sorted(counts.items(), key=lambda x: x[1], reverse=True)

    return counts_arr


def map_to_frequencies(words_count, all_words_count):
    return [(count[0], count[1] / all_words_count) for count in words_count]


def count_words_in_book(counts_arr):
    result = 0

    for word_with_count in counts_arr:
        result += word_with_count[1]
    return result
