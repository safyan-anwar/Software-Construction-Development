from validation import validate_mark, INVALID_MARK_MESSAGE
from calculations import calculate_total, calculate_average, calculate_grade
from display import display_result
NUMBER_OF_SUBJECTS = 3
def read_mark(subject_number):
    """Ask for one mark and keep asking until it is valid."""
    mark = float(input(f"Enter marks for subject {subject_number}: "))

    while not validate_mark(mark):
        print(INVALID_MARK_MESSAGE)
        mark = float(input(f"Enter marks for subject {subject_number}: "))
    return mark
def read_all_marks():
    """Collect marks for all subjects."""
    marks = []
    for i in range(NUMBER_OF_SUBJECTS):
        marks.append(read_mark(i + 1))
    return marks
def main():
    name = input("Enter student name: ")
    marks = read_all_marks()

    total = calculate_total(marks)
    average = calculate_average(marks)
    grade = calculate_grade(average)
    display_result(name, total, average, grade)
if __name__ == "__main__":
    main()