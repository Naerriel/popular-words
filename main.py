#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from src.book.book import get_book
from src.clean import clean_words
from src.chart import generate_chart
from src.books_urls import get_urls

books = get_urls()

# file = open('book.txt', 'r')
# words = clean_words(file.read())
# popular_words = generate_chart(words)


def main():
    for book in books:
        book_content = get_book(book[0])
        words = clean_words(book_content)
        popular_words = generate_chart(words)
        return popular_words
