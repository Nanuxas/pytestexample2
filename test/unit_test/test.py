import pytest

def is_palindrome(word):
    new_word = str(word).upper()
    return new_word[::-1] == new_word

def test_palindrome_tuscias():
    assert is_palindrome("")

def test_palindrome_skaicius():
    assert is_palindrome(121)

def test_palindrome_ne_palindrome():
    assert not is_palindrome("abc")

def test_palindrome_su_tarpais():
    assert is_palindrome("is si")

def test_palindrome_didziosios_mazosios():
    assert is_palindrome("Bob")

def test_palindrome_vienas_simbolis():
    assert is_palindrome("a")

def test_palindrome_ar_tikrai_palendromas_veikia():
    assert is_palindrome("bob")
