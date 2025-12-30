def invert_dictionary(original_dict):
    inverted = {}
    for key, value in original_dict.items():
        if value not in inverted:
            inverted[value] = [key]
            inverted[value].append(key)
    return inverted


def main():
    grades = {"John": "A", "Sara": "B", "Musa": "A"}
    inverted_grades = invert_dictionary(grades)
    print(inverted_grades)


if __name__ == "__main__":
    main()
