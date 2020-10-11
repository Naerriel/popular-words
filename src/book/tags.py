#!/usr/bin/env python3

# get_tags is a function which gets a BeautifulSoup and returns it's tags in the format of:
# (name, tag classes, text in this tag)


def get_class(soup_tag):
    result = ''
    for class_name in soup_tag.get_attribute_list('class'):
        result += class_name or ''
    return result


def parse_tag(soup_tag):
    # parsed tag has following structure:
    # (name, classes, text in this tag)
    return (soup_tag.name, soup_tag.name + get_class(soup_tag),
            " ".join(soup_tag.find_all(text=True, recursive=False)))


def are_tags_same(tag1, tag2):
    return tag1[0] == tag2[0] and tag1[1] == tag2[1]


def is_tag_styling(tag):
    return tag[0] in ['a', 'i', 'strong', 'b', 'span']


def get_tags(soup):
    all_tags = soup.find_all()
    tags = [parse_tag(all_tags[0])]

    for tag in all_tags:
        parsed_tag = parse_tag(tag)
        last_tag = tags.pop()

        if are_tags_same(last_tag, parsed_tag) or is_tag_styling(parsed_tag):
            tags.append(
                (last_tag[0], last_tag[1], last_tag[2] + parsed_tag[2]))
        else:
            tags.append(last_tag)
            tags.append(parsed_tag)

    return tags
