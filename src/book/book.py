#!/usr/bin/env python3
from src.book.tags import get_tags
import requests
from bs4 import BeautifulSoup


def get_chars_per_tag(tags):
    chars_per_tag = {}

    for tag in tags:
        tag_name = tag[1]
        if not tag_name in chars_per_tag:
            chars_per_tag[tag_name] = 0

        chars_per_tag[tag_name] += len(tag[2])
    return chars_per_tag


def get_popular_tags(chars_per_tag):
    tags_to_skip = ['style', 'pre', 'h1', 'h2', 'h3', 'li']

    max_chars = 0
    for tag_name in chars_per_tag:
        max_chars = max(max_chars, chars_per_tag[tag_name])

    result = []
    for tag_name in chars_per_tag:
        if chars_per_tag[
                tag_name] * 100 > max_chars and not tag_name in tags_to_skip:
            result.append(tag_name)
    return result


def get_content(tags):
    tags_with_content = get_popular_tags(get_chars_per_tag(tags))
    content = ''
    fillers_length = 0
    last_content = ''
    best_content = ''

    for tag in tags:
        if tag[1] in tags_with_content:
            content += tag[2]
            fillers_length = 0
        else:
            last_content = content  # Clearing up the content. If the fillers are long enough, I'll delete the content for good
            content = ''
            fillers_length += len(tag[2])

        if fillers_length < 100 and len(content) < len(last_content):
            content = last_content
            last_content = ''

        if len(content) > len(best_content):
            best_content = content
    return best_content


def get_book(url):
    soup = BeautifulSoup(requests.get(url).text, 'html.parser')
    tags = get_tags(soup)
    return get_content(tags)