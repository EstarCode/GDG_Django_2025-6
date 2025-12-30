def read_and_uppercase(filename):
    try:
        with open(filename, "r") as file:
            message = file.read()
            upper_content = message.upper()
            print(upper_content)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")


def main():
    return (read_and_uppercase("message.txt"))


if __name__ == "__main__":
    main()
