# Git & GitHub Workshop for Beginners

This repository contains the presentation slides, hands-on exercises, and demo code used in the **Git & GitHub Workshop** conducted for students at DIT.

The goal of this workshop is to help beginners understand **why Git exists**, overcome the fear of using it, and confidently start managing their projects with Git and GitHub.

---

# 📚 Contents

```
.
├── Presentation/      # Workshop slides
├── Hands-On/          # Demo projects and exercises
└── README.md
```

---

# 🎯 Workshop Agenda

* Why developers fear Git
* Life before Version Control
* The story behind Git
* Git vs GitHub
* Understanding the Git workflow
* Hands-on with Git
* Pushing your first repository to GitHub
* Exploring the open-source ecosystem

---

# 🛠️ Prerequisites

Before starting, install:

* Git
* VS Code (Recommended)
* A GitHub account

Verify your installation:

```bash
git --version
```

---

# 💻 Hands-on Exercises

The workshop includes practical exercises covering:

## Exercise 1

Initialize your first repository.

```bash
mkdir GitWorkshop
cd GitWorkshop
git init
```

---

## Exercise 2

Check repository status.

```bash
git status
```

---

## Exercise 3

Track a new file.

```bash
git add README.md
```

---

## Exercise 4

Create your first commit.

```bash
git commit -m "Initial commit"
```

---

## Exercise 5

View commit history.

```bash
git log
```

---

## Exercise 6

Push to GitHub.

```bash
git remote add origin <repository-url>
git branch -M main
git push -u origin main
```

---

# 🧠 Git Workflow

```
Working Directory
        │
        ▼
   git add
        │
        ▼
 Staging Area
        │
        ▼
  git commit
        │
        ▼
 Local Repository
        │
        ▼
   git push
        │
        ▼
     GitHub
```

---

# 📖 Commands Covered

| Command      | Purpose                     |
| ------------ | --------------------------- |
| `git init`   | Create a Git repository     |
| `git status` | View current changes        |
| `git add`    | Stage changes               |
| `git commit` | Save a snapshot             |
| `git log`    | View commit history         |
| `git clone`  | Copy an existing repository |
| `git push`   | Upload changes to GitHub    |
| `git pull`   | Download latest changes     |

---

# 🌍 Popular Open Source Projects

During the workshop, we'll explore how GitHub powers some of the world's most impactful software projects, including:

* Linux
* VS Code
* React
* PyTorch
* Python
* LangChain
* Kubernetes
* TensorFlow

---

# 🎯 Learning Outcomes

By the end of this workshop, you'll be able to:

* Understand Version Control
* Create and manage Git repositories
* Track project history
* Push code to GitHub
* Collaborate using GitHub
* Start contributing to Open Source