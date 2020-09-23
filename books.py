#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup


def get_book(url):
	return requests.get(url).text


	# chapters = soup.find_all('div', class_='chapter')


	# result = []

	# for chapter in chapters:
		# text = chapter.get_text().encode('utf-8')
		# result.append(text)

	# return ''.join(result)

def parse_tag(soupTag):
	# parsed tag has following structure:
	# (name, classes, length of text in those tags)
	return (soupTag.name, soupTag.get_attribute_list('class'), soupTag.find(text=True, recursive=False) or '')

def are_tags_same(tag1, tag2):
	return tag1[0] == tag2[0] and tag1[1] == tag2[1]

def is_tag_styling(tag):
	return tag[0] in ['a', 'i', 'strong', 'b', 'span']

def parse_tags(soup):
	all_tags = soup.find_all()
	tags = [parse_tag(all_tags[0])]

	for tag in all_tags:
		parsed_tag = parse_tag(tag)
		last_tag = tags.pop()

		if are_tags_same(last_tag, parsed_tag) or is_tag_styling(parsed_tag):
			tags.append(
				(last_tag[0], last_tag[1], last_tag[2] + parsed_tag[2])
			)
		else:
			tags.append(last_tag)
			tags.append(parsed_tag)

	return tags

def get_chars_per_tag(tags):
	chars_per_tag = {}

	for tag in tags:
		tag_name = tag[0]
		if not tag_name in chars_per_tag:
			chars_per_tag[tag_name] = 0

		chars_per_tag[tag_name] += len(tag[2])
	return chars_per_tag

def get_popular_tags(chars_per_tag):
	result = []
	for tag_name in chars_per_tag:
		if chars_per_tag > 100 and not tag_name in ['style', 'pre', 'h1', 'h2', 'h3', 'li']:
			result.append(tag_name)
	return result

def get_tags_with_content(tags):
	chars_per_tag = get_chars_per_tag(tags)
	return get_popular_tags(chars_per_tag)

def get_content(tags):
	tags_with_content = get_tags_with_content(tags)
	result = ''

	for tag in tags:
		if tag[0] in tags_with_content:
			result += tag[2]
	return result


def parse_book(bookHTML):
	soup = BeautifulSoup(bookHTML, 'html.parser')
	tags = parse_tags(soup)
	content = get_content(tags)

	print(content[:1000])

	# print(tags)
	# print(tags[500:530])
