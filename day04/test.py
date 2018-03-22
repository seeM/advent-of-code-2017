from passphrase import (
	has_duplicate,
	check_phrases,
	has_anagram,
	check_phrases_anagram
)

TEST_FILE = 'test_phrases.txt'
TEST_FILE2 = 'test_phrases2.txt'

def test_has_duplicate():
	assert has_duplicate('aa bb cc dd ee') == False
	assert has_duplicate('aa bb cc dd aa') == True
	assert has_duplicate('aa bb cc dd aaa') == False

def test_check_phrases():
	assert check_phrases(TEST_FILE) == 4

def test_has_anagram():
	assert has_anagram('abcde fghij') == False
	assert has_anagram('abcde xyz ecdab') == True
	assert has_anagram('a ab abc abd abf abj') == False
	assert has_anagram('iiii oiii ooii oooi oooo') == False
	assert has_anagram('oiii ioii iioi iiio') == True

def test_check_phrases_anagram():
	assert check_phrases_anagram(TEST_FILE2) == 3

test_has_duplicate()
test_check_phrases()
test_has_anagram()
test_check_phrases_anagram()
