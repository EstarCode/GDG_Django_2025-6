def main():
    scores = {"John": 85, "Sara": 92, "Fraol": 78}

    student_name = input("Enter student name: ")

    try:
        print(f"{student_name}'s score is: {scores[student_name]}")
    except KeyError:
        print("Student not found!")


main()
