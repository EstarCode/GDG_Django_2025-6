def is_palindrome(x):
    return x == x[:: -1]


def main():
    x = input("X: ")
    print(is_palindrome(x))


main()
