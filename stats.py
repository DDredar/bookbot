def text_file_word_count(book_path):
	with open(book_path) as f:
		book_contents = f.read()
	words_in_book = len(book_contents.split())
	return words_in_book

def letter_counts(book_path):
	with open(book_path) as f:
		book_contents = f.read().lower()
	letter_dictionary = {"e": 0, "t": 0,} # "a": 0,
# "o": 0, "i": 0, "n": 0, "s": 0, "r": 0, "h": 0, "d": 0, "l": 0,
# "m": 0, "u": 0, "c": 0, "f": 0, "y": 0, "w": 0, "p": 0, "g": 0,
# "b": 0, "v": 0, "k": 0, "x": 0, "j": 0, "q": 0, "z": 0, "æ": 0,
# "â": 0, "ê": 0, "ë": 0, "ô": 0}

	for key in letter_dictionary:
		number_of_letters = 0
		for letters in book_contents:
			if letters == key:
				number_of_letters += 1
			letter_dictionary[key] = number_of_letters

	return letter_dictionary
