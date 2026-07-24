# Git Hands-On Guide

Work through these steps from the `Hands-On` folder. Type each command yourself and read its output before moving on.

> This exercise changes Git history locally. Do not run `git push`, and do not use `git rebase` on a shared branch unless your instructor tells you to.

## 1. Check the starting point

```bash
git status
git branch --show-current
python3 app.py
```

`git status` tells you which files Git sees as new, changed, or ready to commit. Run it often.

## 2. Inspect the existing history

```bash
git log --oneline --graph --all
git branch --all
```

Each line in the log is a **commit**: a saved checkpoint. A **branch** is a named line of work that points to commits.

## 3. Make and commit a small change

Open `README.md`. Add your name below the title, for example:

```md
Prepared by: Your Name
```

Now inspect and save the change:

```bash
git status
git diff
git add README.md
git status
git commit -m "Add student name to README"
```

The three important places are:

1. **Working directory** — files you are editing.
2. **Staging area** — selected changes after `git add`.
3. **Repository history** — saved checkpoints after `git commit`.

Check that your commit exists:

```bash
git log --oneline -5
```

## 4. Create a feature branch

Create a branch for a small improvement:

```bash
git switch -c feature/welcome-message
git branch
```

In `app.py`, add this line immediately after the `def main():` line:

```python
    print("Welcome to the Student Marks Calculator")
```

Run the program, inspect the change, and commit it:

```bash
python3 app.py
git diff
git add app.py
git commit -m "Add welcome message"
```

## 5. Merge the feature into `main`

Move back to the main branch and merge your completed feature:

```bash
git switch main
git merge --no-ff feature/welcome-message -m "Merge welcome message"
git log --oneline --graph --all
```

`--no-ff` asks Git to create a merge commit, making the branch-and-merge story clear in the graph.

## 6. Practise rebase

Create another feature branch and make one small change:

```bash
git switch -c feature/student-count
```

In `app.py`, add this line after the line that prints the student names:

```python
    print(f"Number of students: {len(STUDENTS)}")
```

Commit it:

```bash
git add app.py
git commit -m "Display number of students"
```

Now make an independent commit on `main`:

```bash
git switch main
```

Add one short sentence anywhere in `README.md`, then run:

```bash
git add README.md
git commit -m "Add study reminder"
```

Rebase the feature onto the latest `main`:

```bash
git switch feature/student-count
git rebase main
git log --oneline --graph --all
```

Rebase replays your feature commit on top of the newest `main`. Merge the rebased feature when it is ready:

```bash
git switch main
git merge --no-ff feature/student-count -m "Merge student count"
```

## 7. See a merge conflict safely

Create two branches that edit the same line differently.

First branch:

```bash
git switch -c feature/heading-a
```

In `app.py`, change the heading text to:

```python
    print("Class Marks Summary")
```

Then commit it:

```bash
git add app.py
git commit -m "Change heading on feature branch"
```

Create a different change on `main`:

```bash
git switch main
```

Change that same heading line to:

```python
    print("Student Results")
```

Commit the main-branch version, then merge the feature:

```bash
git add app.py
git commit -m "Change heading on main"
git merge feature/heading-a
```

Git should report a conflict. Open `app.py`; you will see markers like:

```text
<<<<<<< HEAD
    print("Student Results")
=======
    print("Class Marks Summary")
>>>>>>> feature/heading-a
```

Replace all those lines with one final choice, for example:

```python
    print("Student Marks Summary")
```

Then finish the merge:

```bash
python3 app.py
git add app.py
git commit -m "Resolve heading conflict"
```

If you want to cancel an unfinished merge instead, use:

```bash
git merge --abort
```

## 8. Useful commands to remember

```bash
git status                       # See the current state
git diff                         # See unstaged edits
git diff --staged                # See staged edits
git log --oneline --graph --all  # See branches and commits
git restore filename.py          # Discard an unstaged change
git switch branch-name           # Change branch
```

## Finish

Run this command and make sure you can explain the graph:

```bash
git log --oneline --graph --all
```

You have practised the core Git workflow: change files, inspect them, stage them, commit them, work on branches, merge work, rebase a private feature branch, and resolve a conflict.
