def get_square_root(x):
    if x < 2:
        return x   # 0: 0, 1 : 1
    left, right = 1, x // 2
    while left <= right:
        mid = (left + right) // 2
        square = mid * mid

        if square == x:
            return mid
        elif square < x:
            left = mid + 1
        else:
            right = mid - 1
    return right   # right is the floor(sqrt(x))


def main():
    num = int(input("Enter any Integer :"))
    result = get_square_root(num)
    print("The square of num: ", result)


if __name__ == "__main__":
    main()
