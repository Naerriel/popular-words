#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from src.book.book import get_book
from src.clean import clean_words
from src.words.main import create_chart
from src.books_urls import get_urls

books = get_urls()


def generate_chart():
    # parsed_book[0] - title, parsed_book[1] - words array
    parsed_books = []

    for book in books:
        book_content = get_book(book[0])
        words = clean_words(book_content)

        parsed_books.append(book[1], words)

    create_chart(parsed_books)


generate_chart()