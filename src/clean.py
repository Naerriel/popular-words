#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import string
from nltk.corpus import stopwords


def clean_words(text):
    clean_text = text.lower()
    clean_text = delete_punctuation(clean_text)
    words = clean_text.split()
    words = delete_stop_words(words)

    return words


def delete_punctuation(text):
    table = str.maketrans('', '', string.punctuation + '—”“”‘’')
    # return [w.translate(table) for w in words]
    return text.translate(table)


def delete_stop_words(words):
    custom_words = [
        'b', '1', 'elizabeth', 'collins', 'elizabeths', 'eliza', 'phillips',
        'â', 'john', 'johns', 'andrew', 'thomas', 'hopkins'
    ]
    stop_words = stopwords.words('english') + custom_words
    return [w for w in words if not w in stop_words]