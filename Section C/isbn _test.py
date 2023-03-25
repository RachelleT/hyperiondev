import unittest
import isbn

class TestIsbnMethods(unittest.TestCase):

    def test_isbn13(self):
        assert isbn.isbn13(25) == "Invalid input type" # test for input type
        assert isbn.isbn13("9780316066525") == "valid" # test for valid isbn13
        assert isbn.isbn13("0330301824") == "invalid" # test for invalid isbn10
        assert isbn.isbn13("0316066524") == "9780316066525" # test for valid isbn10
        assert isbn.isbn13("978031606652X") == "invalid" # test for isbn13 with X

    def test_checkIsbn13(self):
        assert (type(isbn.checkIsbn13([9, 7, 8, 0, 3, 1, 6, 0, 6, 6, 5, 2, 5])) == list) # test return type

    def test_stringIsbn13(self):
        assert (type(isbn.stringIsbn13([9, 7, 8, 0, 3, 1, 6, 0, 6, 6, 5, 2, 5])) == str) # test return type

if __name__ == '__main__':
    unittest.main()

