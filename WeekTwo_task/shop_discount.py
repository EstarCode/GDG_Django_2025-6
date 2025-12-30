def discount():
    numberOfItem = int(input("Enter the number of items wanted to buy: "))
    if numberOfItem > 3:
        print("Discount applied")
    else:
        print("No discount")


discount()
