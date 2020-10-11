#!/usr/bin/env python3


def generate_chart(words):
    counts = {}
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    countsArr = sorted(counts.items(), key=lambda x: x[1], reverse=True)

    return countsArr[:20]