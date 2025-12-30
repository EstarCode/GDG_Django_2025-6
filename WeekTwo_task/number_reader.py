def sum_valid_numbers():
    total = 0
    try:
        with open("numbers.txt", "r") as file:
            for line in file:
                clean = line.strip()

                try:
                    number = int(clean)
                    total += number
                except ValueError:
                    # Skip invalid lines (like "abc")
                    print(f"Skipping invalid entry: {clean}")

        print("Sum =", total)

    except FileNotFoundError:
        print("Error: numbers.txt not found")


sum_valid_numbers()
