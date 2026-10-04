def process_student(name, marks):
    if len(marks) == 0:
        return "Invalid marks."
    for mark in marks:
        if mark < 0 or mark > 100:
            return "Invalid marks."
    total_marks = sum(marks)
    average_marks = total_marks / len(marks)
    if average_marks >= 85:
        grade = "A"
    elif average_marks >= 75:
        grade = "A-"
    elif average_marks >= 70:
        grade = "B"
    elif average_marks >= 60:
        grade = "C"
    else:
        grade = "F"

    result = (
        f"Student name: {name}\n"
        f"Marks: {marks}\n"
        f"Total marks: {total_marks}\n"
        f"Average marks: {average_marks:.2f}\n"
        f"Grade: {grade}"
    )
    print(result)
    with open("student_result.txt", "w") as file:
        file.write(result)
student_name = "Safyan"
student_marks = [80, 75, 90, 85, 70]
process_student(student_name, student_marks)

