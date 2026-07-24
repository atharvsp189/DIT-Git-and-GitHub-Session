"""A tiny student marks calculator for a Git teaching demo."""


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
    marks = [70, 82, 91]
    average = calculate_average(marks)
    print("Student Marks Calculator")
    print(f"Class average: {average:.1f}")
    print(f"Grade for the average: {calculate_grade(average)}")


if __name__ == "__main__":
    main()
