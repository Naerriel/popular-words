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

def get_class(soup_tag):
	result = ''
	for class_name in soup_tag.get_attribute_list('class'):
		result += class_name or ''
	return result

def parse_tag(soup_tag):
	# parsed tag has following structure:
	# (name, classes, length of text in those tags)
	return (soup_tag.name, soup_tag.name + get_class(soup_tag), soup_tag.find(text=True, recursive=False) or '')

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
		tag_name = tag[1]
		if not tag_name in chars_per_tag:
			chars_per_tag[tag_name] = 0

		chars_per_tag[tag_name] += len(tag[2])
	return chars_per_tag

def get_popular_tags(chars_per_tag):
	max_chars = 0
	for tag_name in chars_per_tag:
		max_chars = max(max_chars, chars_per_tag[tag_name])

	result = []
	for tag_name in chars_per_tag:
		if chars_per_tag[tag_name] * 100 > max_chars and not tag_name in ['style', 'pre', 'h1', 'h2', 'h3', 'li']:
			result.append(tag_name)
	return result

def get_tags_with_content(tags):
	chars_per_tag = get_chars_per_tag(tags)
	print('chars per tag = ', chars_per_tag)
	return get_popular_tags(chars_per_tag)

def get_content(tags):
	tags_with_content = get_tags_with_content(tags)
	print('tags with content = ', tags_with_content)
	content = ''
	fillers_length = 0
	last_content = ''
	best_content = ''

	for tag in tags:
		print(len(content), len(last_content), fillers_length)
		if tag[1] in tags_with_content:
			content += tag[2]
			fillers_length = 0
		else:
			last_content = content # Clearing up the content. If the fillers are long enough, I'll delete the content for good
			content = ''
			fillers_length += len(tag[2])

		if fillers_length < 100 and len(content) < len(last_content):
			content = last_content
			last_content = ''

		if len(content) > len(best_content):
			best_content = content
	return best_content

def parse_book(bookHTML):
	soup = BeautifulSoup(bookHTML, 'html.parser')
	tags = parse_tags(soup)
	content = get_content(tags)

	print content[:1000]
	print content[-1000:]

	# print(tags)
	# print(tags[500:530])
