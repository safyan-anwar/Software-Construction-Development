def calculate_total(marks):
    """Return the sum of all marks."""
    return sum(marks)
def calculate_average(marks):
    """Return the average of the marks."""
    return calculate_total(marks) / len(marks)
def calculate_grade(average):
    """Convert an average into a letter grade."""
    if average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"