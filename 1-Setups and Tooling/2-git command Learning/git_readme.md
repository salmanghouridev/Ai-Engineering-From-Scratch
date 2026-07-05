# 🚀 Git & GitHub — Complete Master Guide

> Your ultimate reference for Git commands — from beginner to advanced.

---

## 📋 Table of Contents

1. [Initial Setup](#1--initial-setup)
2. [Creating a Repository](#2--creating-a-repository)
3. [Basic Workflow (Add, Commit, Push)](#3--basic-workflow-add-commit-push)
4. [Branching](#4--branching)
5. [Merging](#5--merging)
6. [Pulling & Fetching](#6--pulling--fetching)
7. [Stashing](#7--stashing)
8. [Undoing Changes](#8--undoing-changes)
9. [Viewing History & Logs](#9--viewing-history--logs)
10. [Tags & Releases](#10--tags--releases)
11. [Remote Repositories](#11--remote-repositories)
12. [GitHub Pull Requests (PR Workflow)](#12--github-pull-requests-pr-workflow)
13. [.gitignore](#13--gitignore)
14. [Advanced Commands](#14--advanced-commands)
15. [Common Workflows](#15--common-workflows)
16. [Cheat Sheet](#16--cheat-sheet)

---

## 1. 🛠 Initial Setup

```bash
# Set your identity (required before first commit)
git config --global user.name "salmanghouridev"
git config --global user.email "your-email@example.com"

# Save credentials so you don't enter token every time (macOS)
git config --global credential.helper osxkeychain

# Check your current config
git config --list

# Check specific settings
git config user.name
git config user.email
```

---

## 2. 📁 Creating a Repository

### Start a NEW project locally
```bash
# Initialize a new git repo in current folder
git init

# Add remote (connect to GitHub)
git remote add origin https://github.com/salmanghouridev/your-repo-name.git

# Push for the first time
git push -u origin main
```

### Clone an EXISTING repo from GitHub
```bash
# Clone a repo (downloads it to your machine)
git clone https://github.com/salmanghouridev/repo-name.git

# Clone into a specific folder
git clone https://github.com/salmanghouridev/repo-name.git my-folder
```

---

## 3. 📤 Basic Workflow (Add, Commit, Push)

This is the workflow you'll use **every day**:

```bash
# Step 1: Check what files changed
git status

# Step 2: Add files to staging area
git add filename.py          # Add a specific file
git add .                    # Add ALL changed files
git add *.py                 # Add all Python files
git add src/                 # Add entire folder

# Step 3: Commit (save a snapshot)
git commit -m "your message here"

# Step 4: Push to GitHub
git push origin main         # Push to main branch
git push                     # Push to current branch (if tracking is set)
```

### 💡 Quick shortcut: Add + Commit in one step
```bash
git commit -am "message"     # Only works for MODIFIED files (not new files)
```

---

## 4. 🌿 Branching

Branches let you work on features without affecting the main code.

### Create & Switch Branches
```bash
# See all branches (* = current branch)
git branch

# See all branches (including remote)
git branch -a

# Create a new branch
git branch feature-login

# Switch to a branch
git checkout feature-login

# ✅ Create AND switch in one command (RECOMMENDED)
git checkout -b feature-login

# Modern alternative (Git 2.23+)
git switch feature-login
git switch -c feature-login   # Create + switch
```

### Rename a Branch
```bash
# Rename current branch
git branch -m new-name

# Rename a specific branch
git branch -m old-name new-name
```

### Delete a Branch
```bash
# Delete local branch (safe — won't delete unmerged work)
git branch -d feature-login

# Force delete local branch
git branch -D feature-login

# Delete remote branch
git push origin --delete feature-login
```

### Push a Branch to GitHub
```bash
# Push new branch to GitHub for the first time
git push -u origin feature-login

# After that, just use:
git push
```

---

## 5. 🔀 Merging

Combine changes from one branch into another.

```bash
# Step 1: Switch to the branch you want to merge INTO
git checkout main

# Step 2: Merge the feature branch into main
git merge feature-login

# Step 3: Push the merged result
git push origin main

# Step 4: (Optional) Delete the merged branch
git branch -d feature-login
git push origin --delete feature-login
```

### Handling Merge Conflicts
```bash
# If merge has conflicts, Git will tell you which files
git status                    # See conflicted files

# Open the file — you'll see conflict markers:
# <<<<<<< HEAD
# your changes
# =======
# their changes
# >>>>>>> feature-login

# Fix the file manually, then:
git add conflicted-file.py
git commit -m "Resolved merge conflict"
```

---

## 6. 📥 Pulling & Fetching

```bash
# Pull = Fetch + Merge (gets latest changes and merges them)
git pull origin main

# Fetch only (downloads changes but doesn't merge)
git fetch origin

# Pull with rebase (cleaner history, no merge commits)
git pull --rebase origin main
```

---

## 7. 📦 Stashing

Temporarily save changes without committing.

```bash
# Stash your current changes
git stash

# Stash with a message
git stash save "work in progress on login"

# List all stashes
git stash list

# Apply the latest stash (keeps it in stash list)
git stash apply

# Apply AND remove from stash list
git stash pop

# Apply a specific stash
git stash apply stash@{2}

# Delete a specific stash
git stash drop stash@{0}

# Delete ALL stashes
git stash clear
```

### 💡 Use Case: Switch branch with uncommitted work
```bash
git stash                    # Save current work
git checkout other-branch    # Switch branch
# ... do work ...
git checkout original-branch # Come back
git stash pop                # Restore your work
```

---

## 8. ↩️ Undoing Changes

### Unstage a file (undo `git add`)
```bash
git reset HEAD filename.py
# or modern way:
git restore --staged filename.py
```

### Discard changes in a file (revert to last commit)
```bash
git checkout -- filename.py
# or modern way:
git restore filename.py
```

### Undo the last commit (keep changes)
```bash
git reset --soft HEAD~1
```

### Undo the last commit (discard changes) ⚠️
```bash
git reset --hard HEAD~1
```

### Undo a specific commit (creates a new "reverse" commit)
```bash
git revert abc1234           # Use commit hash
```

### Amend the last commit message
```bash
git commit --amend -m "corrected message"
```

### Amend last commit (add forgotten files)
```bash
git add forgotten-file.py
git commit --amend --no-edit  # Keeps the same message
```

---

## 9. 📜 Viewing History & Logs

```bash
# View commit history
git log

# Compact one-line view
git log --oneline

# Show last 5 commits
git log -5

# Visual branch graph
git log --oneline --graph --all

# See what changed in each commit
git log -p

# See changes in a specific file
git log --follow filename.py

# Show who changed each line of a file
git blame filename.py

# See difference between working directory and last commit
git diff

# See difference between staged and last commit
git diff --staged

# Compare two branches
git diff main..feature-login

# Show details of a specific commit
git show abc1234
```

---

## 10. 🏷 Tags & Releases

Tags mark specific points in history (e.g., versions).

```bash
# Create a lightweight tag
git tag v1.0.0

# Create an annotated tag (recommended)
git tag -a v1.0.0 -m "Version 1.0.0 - Initial release"

# Tag a specific commit
git tag -a v1.0.0 abc1234 -m "Tagging old commit"

# List all tags
git tag

# Push a tag to GitHub
git push origin v1.0.0

# Push ALL tags
git push origin --tags

# Delete a local tag
git tag -d v1.0.0

# Delete a remote tag
git push origin --delete v1.0.0
```

---

## 11. 🌐 Remote Repositories

```bash
# View remotes
git remote -v

# Add a remote
git remote add origin https://github.com/salmanghouridev/repo.git

# Change remote URL
git remote set-url origin https://github.com/salmanghouridev/new-repo.git

# Remove a remote
git remote remove origin

# Rename a remote
git remote rename origin upstream
```

---

## 12. 🔄 GitHub Pull Requests (PR Workflow)

This is how teams collaborate on GitHub:

```bash
# Step 1: Create a branch for your feature
git checkout -b feature-awesome

# Step 2: Make changes, add, commit
git add .
git commit -m "Add awesome feature"

# Step 3: Push branch to GitHub
git push -u origin feature-awesome

# Step 4: Go to GitHub → your repo
#         You'll see "Compare & pull request" button
#         Click it → write description → Create PR

# Step 5: After PR is approved and merged on GitHub,
#         update your local main
git checkout main
git pull origin main

# Step 6: Clean up
git branch -d feature-awesome
```

---

## 13. 📄 .gitignore

Create a `.gitignore` file to tell Git which files to ignore.

```bash
# Create .gitignore file
touch .gitignore
```

### Common `.gitignore` entries:
```gitignore
# Python
__pycache__/
*.pyc
*.pyo
.env
venv/
*.egg-info/

# Node.js
node_modules/
dist/
.env

# IDE
.vscode/
.idea/
*.swp

# OS files
.DS_Store
Thumbs.db

# Jupyter
.ipynb_checkpoints/

# Logs
*.log
```

### Check what's being ignored
```bash
git status --ignored
```

---

## 14. 🧠 Advanced Commands

### Cherry-Pick (apply a specific commit to current branch)
```bash
git cherry-pick abc1234
```

### Rebase (rewrite commit history for clean linear history)
```bash
git checkout feature-branch
git rebase main

# Interactive rebase (squash, reorder, edit commits)
git rebase -i HEAD~3        # Last 3 commits
```

### Squash Commits (combine multiple commits into one)
```bash
git rebase -i HEAD~3
# In the editor, change "pick" to "squash" (or "s") for commits to combine
# Save and edit the combined commit message
```

### Reset Remote to Match Local
```bash
git push --force origin main  # ⚠️ Dangerous — overwrites remote history
git push --force-with-lease origin main  # Safer alternative
```

### Clean Untracked Files
```bash
git clean -n                 # Preview what will be deleted
git clean -f                 # Delete untracked files
git clean -fd                # Delete untracked files AND directories
```

### Bisect (find which commit introduced a bug)
```bash
git bisect start
git bisect bad               # Current commit is bad
git bisect good abc1234      # This old commit was good
# Git will checkout commits for you to test
git bisect good              # or git bisect bad
# Repeat until bug commit is found
git bisect reset             # Done
```

---

## 15. 🗑 Remove Git Repository

Sometimes you need to remove Git tracking or disconnect from GitHub.

### Remove Git completely from a project (local)
```bash
# This removes ALL git history — your project becomes a normal folder
rm -rf .git
```

### Remove remote connection only (keep local git)
```bash
# Disconnect from GitHub but keep local commits
git remote remove origin

# Verify remote is removed
git remote -v                # Should show nothing
```

### Delete a repo from GitHub
```
Go to GitHub → Your Repo → Settings → Scroll to bottom
→ "Danger Zone" → "Delete this repository"
```

### Re-initialize and connect to a NEW repo
```bash
# Step 1: Remove old git
rm -rf .git

# Step 2: Start fresh
git init
git add .
git commit -m "Initial commit"

# Step 3: Connect to new GitHub repo
git remote add origin https://github.com/salmanghouridev/new-repo.git
git branch -M main
git push -u origin main
```

### Switch to a different GitHub repo (keep history)
```bash
# Just change the remote URL
git remote set-url origin https://github.com/salmanghouridev/different-repo.git
git push -u origin main
```

---

## 16. 🔄 Common Workflows

### 🟢 Daily Workflow (Solo Developer)
```bash
git pull origin main         # Get latest
# ... make changes ...
git add .
git commit -m "description"
git push origin main
```

### 🟡 Feature Branch Workflow (Team)
```bash
git checkout main
git pull origin main
git checkout -b feature-x    # New branch
# ... make changes ...
git add .
git commit -m "Add feature X"
git push -u origin feature-x
# → Create PR on GitHub
# → After merge, clean up:
git checkout main
git pull origin main
git branch -d feature-x
```

### 🔴 Hotfix Workflow (Urgent Fix)
```bash
git checkout main
git pull origin main
git checkout -b hotfix-bug
# ... fix the bug ...
git add .
git commit -m "Fix critical bug"
git push -u origin hotfix-bug
# → Create PR → Merge immediately
```

---

## 17. 📋 Cheat Sheet

### 🟢 Setup & Init
| Command | Description |
|---------|-------------|
| `git init` | Initialize new repo |
| `git clone <url>` | Clone a repo |
| `git config --global user.name "name"` | Set username |
| `git config --global user.email "email"` | Set email |
| `git config --list` | View all config |

### 📤 Basic Workflow
| Command | Description |
|---------|-------------|
| `git status` | Check status of files |
| `git add <file>` | Stage a specific file |
| `git add .` | Stage ALL changes |
| `git add *.py` | Stage all Python files |
| `git commit -m "msg"` | Commit staged changes |
| `git commit -am "msg"` | Add + commit modified files |
| `git push` | Push to remote |
| `git push -u origin main` | Push & set upstream tracking |
| `git pull` | Pull latest from remote |
| `git pull --rebase` | Pull with rebase (cleaner) |
| `git fetch` | Download changes (don't merge) |

### 🌿 Branching
| Command | Description |
|---------|-------------|
| `git branch` | List all local branches |
| `git branch -a` | List all branches (local + remote) |
| `git branch <name>` | Create a new branch |
| `git checkout -b <name>` | Create & switch to new branch |
| `git checkout <branch>` | Switch to existing branch |
| `git switch <branch>` | Switch branch (modern) |
| `git switch -c <name>` | Create & switch (modern) |
| `git branch -m <new-name>` | Rename current branch |
| `git branch -d <name>` | Delete branch (safe) |
| `git branch -D <name>` | Force delete branch |
| `git push origin --delete <name>` | Delete remote branch |
| `git push -u origin <branch>` | Push new branch to GitHub |

### 🔀 Merging & Rebasing
| Command | Description |
|---------|-------------|
| `git merge <branch>` | Merge branch into current |
| `git rebase main` | Rebase onto main |
| `git rebase -i HEAD~3` | Interactive rebase (squash etc.) |
| `git cherry-pick <hash>` | Apply specific commit |

### ↩️ Undoing Changes
| Command | Description |
|---------|-------------|
| `git restore <file>` | Discard file changes |
| `git restore --staged <file>` | Unstage a file |
| `git reset --soft HEAD~1` | Undo last commit (keep changes) |
| `git reset --hard HEAD~1` | Undo last commit (delete changes) ⚠️ |
| `git revert <hash>` | Reverse a commit (safe) |
| `git commit --amend -m "msg"` | Edit last commit message |

### 📦 Stashing
| Command | Description |
|---------|-------------|
| `git stash` | Save work temporarily |
| `git stash save "message"` | Stash with description |
| `git stash list` | List all stashes |
| `git stash pop` | Restore & remove stash |
| `git stash apply` | Restore & keep stash |
| `git stash drop` | Delete a stash |
| `git stash clear` | Delete ALL stashes |

### 📜 History & Inspection
| Command | Description |
|---------|-------------|
| `git log` | View commit history |
| `git log --oneline` | Compact history |
| `git log --oneline --graph --all` | Visual branch graph |
| `git log -5` | Last 5 commits |
| `git diff` | View unstaged changes |
| `git diff --staged` | View staged changes |
| `git diff main..feature` | Compare two branches |
| `git blame <file>` | See who changed each line |
| `git show <hash>` | Show commit details |

### 🌐 Remote & Repos
| Command | Description |
|---------|-------------|
| `git remote -v` | View remotes |
| `git remote add origin <url>` | Add remote |
| `git remote set-url origin <url>` | Change remote URL |
| `git remote remove origin` | Remove remote connection |
| `rm -rf .git` | Remove git completely ⚠️ |

### 🏷 Tags
| Command | Description |
|---------|-------------|
| `git tag` | List all tags |
| `git tag -a v1.0 -m "msg"` | Create annotated tag |
| `git push origin v1.0` | Push tag to GitHub |
| `git push origin --tags` | Push all tags |
| `git tag -d v1.0` | Delete local tag |

### 🧹 Cleanup
| Command | Description |
|---------|-------------|
| `git clean -n` | Preview untracked file deletion |
| `git clean -f` | Delete untracked files |
| `git clean -fd` | Delete untracked files & dirs |
| `git push --force-with-lease` | Safe force push |

---

## 🎯 Golden Rules

1. **Commit often** — Small, focused commits are easier to understand and revert
2. **Write meaningful commit messages** — `"Fix login bug"` > `"fix stuff"`
3. **Pull before push** — Always `git pull` before `git push` to avoid conflicts
4. **Never force push to main** — Use `--force-with-lease` if you must
5. **Use branches** — Never commit directly to `main` in team projects
6. **Review your changes** — Run `git diff` before committing
7. **Don't commit secrets** — No API keys, tokens, or passwords in code!

---

> Made with ❤️ by [salmanghouridev](https://github.com/salmanghouridev)
