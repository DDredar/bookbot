import sys

def main():


	if len(sys.argv) > 1:

		book_path = sys.argv[1]
		from stats import text_file_word_count
		from stats import letter_counts

		word_count = text_file_word_count(book_path)
		letter_totals = letter_counts(book_path)


		#print("============ BOOKBOT ============")
		#print("Analyzing book found at books/frankenstein.txt...")
		#print("----------- Word Count ----------")
		#print(f"Found {word_count} total words")
		#print("--------- Character Count -------")

		for key, value in letter_totals.items():
			print(f"{key}: {value}")

		#print("============= END ===============")
	else:

		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
main()
