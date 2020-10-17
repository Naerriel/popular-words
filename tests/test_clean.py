#!/usr/bin/env python3

import src.clean


def test_clean_words():
    text = '''Text with, some punctuation: which isn't great.=)'''
    res = src.clean.clean_words(text)
    assert res[1] == 'punctuation'
    assert len(res) == 4


def test_delete_punctuation():
    text = '''Text with, some punctuation: which isn't ‘’great.=)'''
    clean_text = src.clean.delete_punctuation(text)
    assert clean_text == 'Text with some punctuation which isnt great'


def test_delete_stop_words():
    words = [
        'me', 'my', 'not_a_stopword_1', 'i', 'you', 'not', 'at', 'mightn\'t',
        'not_a_stopword_2', 'only'
    ]
    words = src.clean.delete_stop_words(words)
    assert len(words) == 2