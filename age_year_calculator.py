from datetime import datetime


def calculate_birth_year():
    age = int(input("Enter your age in years: "))
    current_year = datetime.today().year
    birth_year = current_year - age
    return birth_year


def main():
    birth_year = calculate_birth_year()
    print(f"You were born in the year: {birth_year}")


main()
