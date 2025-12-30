def process_sales_file():
    valid_sales = []

    # Step A: Read sales.txt line by line
    try:
        with open("sales.txt", "r") as file:
            for line in file:
                # Remove extra spaces or newline characters
                clean_line = line.strip()

                try:
                    # Step B: Convert valid lines to integers
                    number = int(clean_line)
                    valid_sales.append(number)

                except ValueError:
                    # Step C: Skip invalid lines like "abc"
                    print(f"Skipping invalid entry: {clean_line}")

    except FileNotFoundError:
        print("Error: sales.txt file not found.")
    total = sum(valid_sales)
    print("\nValid Sales Numbers:", valid_sales)
    print("Total Sales:", total)


process_sales_file()
