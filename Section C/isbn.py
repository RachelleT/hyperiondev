# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import numpy as np

def isbn13(isbn):
    if type(isbn) != str:
        return "Invalid input type"
    isbn10code = list(reversed(range(1, 11)))
    if isbn[-1] == "X":  # checks if X is present is isbn
        tempisbn = isbn[:-1]  # stores isbn temporary without X
        isbnlist = [int(x) for x in list(tempisbn)]  # converts isbn to list
        isbn = isbnlist + [10]  # replaces X with 10
    else:
        isbn = [int(x) for x in list(isbn)]  # converts isbn to list
    if len(isbn) == 10:
        result = sum(list(np.multiply(isbn, isbn10code))) % 11  # calculation check for isbn10
        if result >= 1:
            return "invalid"
        else:
            # convert isbn10 to isbn 13
            isbn13 = [9, 7, 8] + isbn
            result = checkIsbn13(isbn13)
            if result[1] == 0:
                return stringIsbn13(isbn13)
            else:
                rounded = round(result[0], -1)
                difference = rounded - result[0]
                isbn13[-1] = isbn13[-1] + difference
                return stringIsbn13(isbn13)
    else:
        # check is isbn13 is valid
        result = checkIsbn13(isbn)
        if result[1] >= 1:
            return "invalid"
        return "valid"

def checkIsbn13(isbn):
    # accepts isbn and returns the results of the isbn13 calculation
    isbn13code = [1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1]
    isbn13sum = sum(list(np.multiply(isbn, isbn13code)))
    result = isbn13sum % 10
    return [isbn13sum, result]

def stringIsbn13(isbn13):
    # accepts isbn13 in a list format and converts it to a string
    newisbn = [str(x) for x in list(isbn13)]
    return "".join(newisbn)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Working.")
    output = isbn13("0316066524")
    print(output)


