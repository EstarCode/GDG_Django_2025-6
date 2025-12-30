def FindMaximum():
    numbers = []

    n = int(input("How many numbers do you want to enter? "))

    for i in range(n):
        num = int(input("Enter a number: "))
        numbers.append(num)

    maximum = numbers[0]

    for num in numbers:
        if num > maximum:
            maximum = num

    print("The maximum number is:", maximum)


FindMaximum()
