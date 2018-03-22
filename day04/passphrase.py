import test

def read_phrases(file):
	"""
	Read phrases from text file into list of strings.
	"""
	phrases = []
	with open(file, 'r') as f:
		return [line[:-1] for line in f]

def has_duplicate(string):
	"""
	Check whether a string contains duplicate words.
	"""
	words = string.split(' ')
	for word in words:
		if words.count(word) > 1:
			return True
	return False

def check_phrases(file):
	"""
	Return the sum of allowable phrases in a list: no duplicate words.
	"""
	phrases = read_phrases(file)
	return sum([not has_duplicate(x) for x in phrases])

def has_anagram(string):
	"""
	Check whether a string has anagrams.
	"""
	words = string.split(' ')
	for i, w in enumerate(words[:-1]):
		for v in words[i + 1:]:
			if len(w) == len(v):
				if sorted(w) == sorted(v):
					return True
	return False


def check_phrases_anagram(file):
	"""
	Return the sum of allowable phrases in a list: no anagrams.
	"""
	phrases = read_phrases(file)
	return sum([not has_anagram(x) for x in phrases])

FILE = 'phrases.txt'

if __name__ == '__main__':
	print(check_phrases(FILE))
	print(check_phrases_anagram(FILE))
