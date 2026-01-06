import sys
def get_book_text(file_path):
	with open(file_path) as f:
		file_contents = f.read()
	return file_contents

def main():
	if len(sys.argv) > 1:
		text = get_book_text(sys.argv[1])
		words = text.split()
		num_of_words = len(words)
		print(f"Found {num_of_words} total words")
	else:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)

def letter_count():
	text = get_book_text(sys.argv[1])
	result = {}
	for letter in text:
		lower = letter.lower()
		if not lower.isalpha():
			continue

		try:
			result[lower] += 1
		except KeyError:
			result[lower] = 1
	return result

def sorting_dict():
	counts = letter_count()
	items = list(counts.items())
	items.sort(key=lambda pair: pair[1], reverse=True)
	for k, v in items:
		print(k + ":", v)

main()
letter_count()
sorting_dict()
