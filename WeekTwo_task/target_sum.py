def two_sum(num, target):
    for i in range(len(num)):
        for j in range(1, len(num)+1):
            if num[i] + num[j] == target:
                return [i, j]


def main():
    nums = [2, 7, 11, 15]
    target = 9
    result = two_sum(nums, target)
    print("target of index: ", result)


if __name__ == "__main__":
    main()
