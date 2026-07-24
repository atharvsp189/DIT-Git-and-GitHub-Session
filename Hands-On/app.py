"""A tiny student marks calculator for a Git teaching demo."""

from students import STUDENTS


def calculate_average(marks):
    """Return the average mark, or 0 when no marks are supplied."""
    return sum(marks) / len(marks) if marks else 0


def calculate_grade(mark):
    """Return a simple letter grade for one mark."""
    if mark >= 90:
        return "A"
    if mark >= 75:
        return "B"
    if mark >= 60:
        return "C"
    return "D"


def main():
    marks = [mark for _, mark in STUDENTS]
    average = calculate_average(marks)
    print("Student Marks Summary")
    print("Students: " + ", ".join(name for name, _ in STUDENTS))
    print(f"Class average: {average:.1f}")
    print(f"Grade for the average: {calculate_grade(average)}")


if __name__ == "__main__":
    main()
