from books import get_book, parse_book

books = [
	('https://www.gutenberg.org/files/1342/1342-h/1342-h.htm', 'Pride and Prejudice'),
	# ('https://www.gutenberg.org/files/16328/16328-h/16328-h.htm', 'Beowulf')
	# ('https://www.gutenberg.org/files/25344/25344-h/25344-h.htm', 'Scarlet Letter')
]

for book in books:
	book_html = get_book(book[0])
	parsed_book = parse_book(book_html)
	print (parsed_book)
