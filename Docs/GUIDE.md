# Build the Student Marks Calculator with Git

This guide recreates the Git history and Python project in this repository. Start in a new empty folder so you can type every command and make every change yourself.

## Before you begin

Check that Git and Python are available:

```bash
git --version
python3 --version
```

If this is your first Git repository, set your name and email once:

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

## 1. Create the project and initialize Git

```bash
mkdir student-marks-calculator
cd student-marks-calculator
git init
git status
```

`git init` creates a Git repository. At this stage, Git has no commits and no project files.

Create a `.gitignore` file with this content:

```text
__pycache__/
*.py[cod]
.venv/
```

This prevents Python cache files and virtual environments from being tracked.

## 2. Write the first version of the program

Create `app.py` with the following code:

```python
"""A tiny student marks calculator"""


def calculate_average(marks):
    """Return the average mark, or 0 when no marks are supplied."""
    return sum(marks) / len(marks) if marks else 0


def main():
    marks = [70, 82, 91]
    average = calculate_average(marks)
    print(f"Class average: {average:.1f}")


if __name__ == "__main__":
    main()
```

Create `README.md` with:

    # Student Marks Calculator

    A small Python project for learning Git.

    ## Run the program

    Run `python3 app.py`.

Run the program:

```bash
python3 app.py
```

Expected output:

```text
Class average: 81.0
```

## 3. Inspect, stage, and commit the initial files

```bash
git status
git add .gitignore README.md app.py
git status
git commit -m "Add initial marks calculator"
git log --oneline
```

`git add` moves selected changes to the staging area. `git commit` saves those staged changes as a checkpoint.

## 4. Add grades on a feature branch

Create and switch to the same feature branch used in this project:

```bash
git switch -c feature/grades
git branch
```

Replace `app.py` with this version. The new `calculate_grade` function converts a numeric mark into a letter grade.

```python
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
```

Test and commit the feature:

```bash
python3 app.py
git diff
git add app.py
git commit -m "Add grade calculation"
```

## 5. Make a change on `main` and merge the feature

Return to `main`:

```bash
git switch main
```

Now merge the grade feature:

```bash
git merge feature/grades -m "Merge grade calculation"
git log --oneline --graph --all
```

The graph now shows two lines of work joining at a merge commit.

## 6. Add named students on another branch

Create a second feature branch:

```bash
git switch -c feature/student-names
```

Create `students.py`:

```python
"""Sample student data used by the Git demo."""

STUDENTS = [
    ("Aarav", 70),
    ("Diya", 82),
    ("Kabir", 91),
]
```

Then replace `app.py` with this version:

```python
"""A tiny student marks calculator"""

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
    print("Student Marks Calculator")
    print("Students: " + ", ".join(name for name, _ in STUDENTS))
    print(f"Class average: {average:.1f}")
    print(f"Grade for the average: {calculate_grade(average)}")


if __name__ == "__main__":
    main()
```

Test and commit:

```bash
python3 app.py
git add app.py students.py
git commit -m "Add named student data"
```

## 7. Rebase the student-names branch

First, make a new commit on `main` while the feature branch is waiting:

```bash
git switch main
```

Add this line to the `README.md` file list:

```md
- `students.py` will contain sample student names after the rebase demo.
```

Commit it:

```bash
git add README.md
git commit -m "Document planned student data"
```

Return to the feature branch and rebase it onto the newest `main`:

```bash
git switch feature/student-names
git rebase main
git log --oneline --graph --all
```

Rebase takes the feature commit and replays it after the latest commit on `main`. This is appropriate for a private branch that only you are using.

Merge the rebased branch:

```bash
git switch main
git merge feature/student-names -m "Merge named student data"
```

## 8. Create and resolve the same merge conflict

Both branches will now change the same heading line in `app.py`.

Create the feature branch:

```bash
git switch -c feature/output-heading
```

Change this line:

```python
print("Student Marks Calculator")
```

to:

```python
print("Class Marks Summary")
```

Commit it:

```bash
git add app.py
git commit -m "Rename output heading on feature branch"
```

Now make a different change to the same line on `main`:

```bash
git switch main
```

Change the heading to:

```python
print("Student Results")
```

Then commit and merge:

```bash
git add app.py
git commit -m "Improve output heading on main"
git merge feature/output-heading
```

Git will stop because it cannot decide which heading to keep. Open `app.py` and replace the conflict markers and both versions with this one final line:

```python
    print("Student Marks Summary")
```

Finish the merge:

```bash
python3 app.py
git add app.py
git commit -m "Resolve output heading conflict"
```

If you need to abandon a merge before committing it, run `git merge --abort`.

## 9. Check your finished project

```bash
python3 app.py
git status
git log --oneline --graph --all
```

Your program should print:

```text
Student Marks Summary
Students: Aarav, Diya, Kabir
Class average: 81.0
Grade for the average: B
```

You have recreated the same project journey: initialization, commits, a feature branch, merge, rebase, merge conflict, and conflict resolution.
