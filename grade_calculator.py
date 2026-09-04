"""
Student Grade Calculator
A simple beginner-friendly program to calculate a student's
total marks, average, and grade based on 3 subjects.
"""


def get_marks(subject_name):
    """Ask the user for marks in one subject, and validate the input."""
    marks = int(input(f"Enter marks in {subject_name}: "))
    while marks < 0 or marks > 100:
        print("Invalid marks! Please enter a value between 0 and 100.")
        marks = int(input(f"Enter marks in {subject_name}: "))
    return marks


def calculate_grade(average):
    """Return a letter grade based on the average marks."""
    if average >= 90:
        return "A"
    elif average >= 75:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 40:
        return "D"
    else:
        return "F"


def print_report(name, marks1, marks2, marks3, total, average, grade):
    """Print a neatly formatted student report."""
    print("\n----- Student Report -----")
    print(f"Name:               {name}")
    print(f"Marks in Subject 1: {marks1}")
    print(f"Marks in Subject 2: {marks2}")
    print(f"Marks in Subject 3: {marks3}")
    print(f"Total Marks:        {total}")
    print(f"Average Marks:      {round(average, 2)}")
    print(f"Grade:              {grade}")
    print("---------------------------")


def main():
    """Main program loop — handles one or more students."""
    print("Welcome to the Student Grade Calculator!")

    while True:
        name = input("\nEnter student name: ")
        marks1 = get_marks("Subject 1")
        marks2 = get_marks("Subject 2")
        marks3 = get_marks("Subject 3")

        total = marks1 + marks2 + marks3
        average = total / 3
        grade = calculate_grade(average)

        print_report(name, marks1, marks2, marks3, total, average, grade)

        again = input("\nCalculate for another student? (yes/no): ")
        if again.lower() != "yes":
            print("\nThank you for using Student Grade Calculator. Goodbye!")
            break


if __name__ == "__main__":
    main()