def get_grade(student_grade, student_name):
    try:
        # Try accessing the student's grade
        grade = student_grade[student_name]
        return grade

    except KeyError:
        # This runs when the student name is not a key in the dictionary
        return "Student not found in the system"


def main():
    grades = {
        "Abel": 90,
        "Sara": 88,
        "Mahi": 92,
        "Noel": 76
    }
    print(get_grade(grades, "Sara"))
    print(get_grade(grades, "Noel"))
    print(get_grade(grades, "Unknown"))


if __name__ == "__main__":
    main()
