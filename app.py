"""A tiny student marks calculator for a Git teaching demo."""


def calculate_average(marks):
    """Return the average mark, or 0 when no marks are supplied."""
    return sum(marks) / len(marks) if marks else 0


def main():
    marks = [70, 82, 91]
    average = calculate_average(marks)
    print(f"Class average: {average:.1f}")


if __name__ == "__main__":
    main()
