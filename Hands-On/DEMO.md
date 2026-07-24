# Git Step-by-Step Guide

This repository is designed for a live beginner-friendly Git demonstration.
Run all commands from the project folder.

## How to use this?

This repository already contains examples of commits, feature branches, merge commits, a rebase, and a resolved conflict. Begin by exploring that history with the commands below. For commands that *change* history (`git switch -c`, `git merge`, and `git rebase`), work in a throwaway copy so that you can repeat the demonstration safely:

```bash
cd ..
cp -a Git-Demo Git-Demo-practice
cd Git-Demo-practice
```

The prepared repository remains your reliable reference; the practice copy is where students can watch new changes happen.

## Before students arrive

```bash
git log --oneline --graph --all
git branch --all
python3 app.py
```

## Part 1: The working area and a commit

```bash
git status
git add app.py README.md .gitignore DEMO.md
git status
git commit -m "Add initial marks calculator"
git log --oneline
```

Explain the three places where a file can be: the working directory, the staging area, and a commit. A commit is a named checkpoint, not merely an automatic save.

## Part 2: A feature branch

```bash
git switch -c feature/grades
git branch
```

On this branch, add a `calculate_grade` function to `app.py` and commit it.

```bash
git add app.py
git commit -m "Add grade calculation"
git switch main
git merge --no-ff feature/grades -m "Merge grade calculation"
```

Explain that a branch is a movable label pointing to a line of commits. `main` was untouched while the feature was being written.

## Part 3: Viewing and comparing work

```bash
git log --oneline --graph --all
git show --stat
git diff main feature/grades
```

## Part 4: Rebase

Create `feature/student-names`, make a commit there, then add another commit to `main`.

```bash
git switch feature/student-names
git rebase main
git log --oneline --graph --all
```

Explain that rebase replays the feature's commits on top of the newest `main`. Do not rebase branches that other people have already pulled unless the team has agreed to it.

## Part 5: Merge conflict

The repository history includes a conflict demonstration: two branches changed the same title line. During a live conflict:

```bash
git status
# Edit the file and remove <<<<<<<, ======= and >>>>>>> markers.
git add app.py
git commit
```

Use `git merge --abort` if you want to cancel an unfinished merge.

## Useful everyday commands

```bash
git status                 # What has changed?
git diff                   # What changed but is not staged?
git diff --staged          # What is staged for the next commit?
git log --oneline --graph --all
git restore filename.py    # Discard an unstaged local edit
git switch branch-name     # Move to another branch
```

## Suggested closing message

Git lets us make small, understandable checkpoints; safely try work on branches; and bring finished work together through merging.
