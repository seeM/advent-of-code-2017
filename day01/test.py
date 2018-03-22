from inverse_captcha import (
    string_to_list,
    matching_digits,
    inverse_captcha,
    matching_digits_halfway,
    inverse_captcha_halfway
)

def test_string_to_list():
    assert string_to_list('1122') == [1, 1, 2, 2]
    assert string_to_list('1111') == [1, 1, 1, 1]
    assert string_to_list('1234') == [1, 2, 3, 4]
    assert string_to_list('91212129') == [9, 1, 2, 1, 2, 1, 2, 9]

def test_matching_digits():
    assert matching_digits([1, 1, 2, 2]) == [1, 2]
    assert matching_digits([1, 1, 1, 1]) == [1, 1, 1, 1]
    assert matching_digits([1, 2, 3, 4]) == []
    assert matching_digits([9, 1, 2, 1, 2, 1, 2, 9]) == [9]

def test_inverse_captcha():
    assert inverse_captcha([1, 1, 2, 2]) == 3
    assert inverse_captcha([1, 1, 1, 1]) == 4
    assert inverse_captcha([1, 2, 3, 4]) == 0
    assert inverse_captcha([9, 1, 2, 1, 2, 1, 2, 9]) == 9

def test_matching_digits_halfway():
    assert matching_digits_halfway([1, 2, 1, 2]) == [1, 2]
    assert matching_digits_halfway([1, 2, 2, 1]) == []
    assert matching_digits_halfway([1, 2, 3, 4, 2, 5]) == [2]
    assert matching_digits_halfway([1, 2, 3, 1, 2, 3]) == [1, 2, 3]

def test_inverse_captcha_halfway():
    assert inverse_captcha_halfway([1, 2, 1, 2]) == 6
    assert inverse_captcha_halfway([1, 2, 2, 1]) == 0
    assert inverse_captcha_halfway([1, 2, 3, 4, 2, 5]) == 4
    assert inverse_captcha_halfway([1, 2, 3, 1, 2, 3]) == 12
    assert inverse_captcha_halfway([1, 2, 1, 3, 1, 4, 1, 5]) == 4

test_string_to_list()
test_matching_digits()
test_inverse_captcha()
test_matching_digits_halfway()
test_inverse_captcha_halfway()
