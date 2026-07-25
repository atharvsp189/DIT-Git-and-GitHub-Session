# How to Authenticate Git with GitHub (Simple & Direct Guide)

Authenticating Git with GitHub allows you to securely push, pull, and manage code repositories from your local command line. GitHub no longer accepts account passwords for Git operations, so you must use either **Personal Access Tokens (HTTPS)** or **SSH Keys**.

---

## Method 1: Personal Access Token (HTTPS) — *Easiest & Quickest*

Use this method if you want a fast setup without managing SSH key files.

### Step 1: Generate a Personal Access Token (PAT)
1. Log in to [GitHub](https://github.com).
2. Click your profile picture in the top-right corner and select **Settings**.
3. Scroll down the left sidebar and click **Developer settings**.
4. Select **Personal access tokens** → **Tokens (classic)**.
5. Click **Generate new token** → **Generate new token (classic)**.
6. Give your token a name (e.g., `My Laptop Git`), choose an expiration period, and select scopes:
   - Check **`repo`** (Full control of private repositories).
7. Scroll down and click **Generate token**.
8. **Copy your token immediately.** *(You won't be able to see it again!)*

### Step 2: Use the Token in Git
When you clone a repository via HTTPS or try to push code:
```bash
git clone https://github.com/username/repository.name.git
```
When prompted:
* **Username:** Enter your GitHub username.
* **Password:** Paste your **Personal Access Token** (NOT your GitHub account password).

---

## Method 2: SSH Keys — *Recommended for Regular Use*

SSH keys provide a secure connection without requiring you to re-enter credentials continuously.

### Step 1: Generate a New SSH Key
Open your terminal (macOS/Linux) or Git Bash (Windows) and run:

```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
```
*Press `Enter` to accept the default file location and optional passphrase prompts.*

### Step 2: Copy the Public Key to Your Clipboard
* **Windows (Git Bash):**
  ```bash
  clip < ~/.ssh/id_ed25519.pub
  ```
* **macOS:**
  ```bash
  pbcopy < ~/.ssh/id_ed25519.pub
  ```
* **Linux:**
  ```bash
  cat ~/.ssh/id_ed25519.pub
  ```
  *(Highlight and copy the displayed output).*

### Step 3: Add the SSH Key to GitHub
1. Go to **GitHub Settings** → **SSH and GPG keys**.
2. Click **New SSH key**.
3. Enter a title (e.g., `Work Laptop`).
4. Keep key type as **Authentication Key**.
5. Paste your public key into the **Key** field.
6. Click **Add SSH key**.

### Step 4: Test the Connection
Run the following command in your terminal:

```bash
ssh -T git@github.com
```
If successful, you will see a message like:
> `Hi username! You've successfully authenticated, but GitHub does not provide shell access.`

---

## Method 3: GitHub CLI (`gh`) — *Automated Setup*

If you have the GitHub CLI installed, you can authenticate in just one command.

1. **Run the login command:**
   ```bash
   gh auth login
   ```
2. Select **GitHub.com**.
3. Choose **HTTPS** or **SSH** as your preferred protocol.
4. Follow the interactive browser prompts to log in and authorize.

---

## Summary Checklist

| Method | Setup Time | Best For |
| :--- | :--- | :--- |
| **PAT (HTTPS)** | ~2 mins | One-off setups, quick access |
| **SSH Key** | ~5 mins | Daily development, long-term security |
| **GitHub CLI** | ~1 min | Command-line power users |
