# Mission 06 — Git and GitHub

## 1. Task / Objective

The objective of this mission is to understand version control, practise staging and committing changes, create and publish a separate branch, understand Pull Requests and explore how GitHub supports collaboration.

## 2. Work Completed

### Task 6.1 — Understand the Basic Git Workflow

I explored the basic Git workflow while working on my Digital Detective assignment repository.

**Git Operations**

| Git Operation | Command | Purpose |
|---|---|---|
| Check repository status | `git status` | Displays modified, staged and untracked files. |
| Stage selected changes | `git add filename` | Selects changes to include in the next commit. |
| Create a commit | `git commit -m "message"` | Records staged changes in the repository history. |
| View commit history | `git log --oneline` | Displays previous commits in a short format. |
| Publish changes | `git push origin main` | Uploads local commits to GitHub. |

**Difference Between Staging and Committing**

Staging is the process of selecting changes that will be included in the next commit.

Committing records the selected changes as a saved version in the Git repository history.

Pushing uploads local commits to the remote GitHub repository.

### Task 6.2 — Create and Use a Branch

A branch allows changes to be made independently without directly affecting the main branch.

**Commands for Creating and Switching to a Branch**

```bash
git branch update-about
git switch update-about
git branch
```

The branch named `update-about` is used to introduce a new My Learning section in the root README.md file.

**My Learning**

Throughout this assignment, I developed an understanding of several important computer science concepts.

1. **Computer Fundamentals and Operating Systems:** I learned how computer hardware, software, processes and system resources work together.

2. **Terminal and Python Programming:** I practised command-line operations, file management, Python programming and number-system conversions.

3. **Version Control and Collaboration:** I learned how Git and GitHub help track changes, maintain project history, manage branches and support collaboration through Pull Requests.

**Commands for Staging, Committing and Publishing the Branch**

```bash
git status
git add README.md
git commit -m "Add learning summary to project README"
git push -u origin update-about
```

The `-u` option establishes an upstream relationship between the local branch and its corresponding remote branch.

### Task 6.3 — Create a Pull Request

A Pull Request allows changes made in one branch to be proposed for inclusion in another branch.

**Pull Request Creation Process**

1. Open the assignment repository on GitHub.
2. Select the Compare & pull request option.
3. Set `main` as the base branch.
4. Set `update-about` as the compare branch.
5. Enter a meaningful title and description.
6. Create the Pull Request and review the proposed changes.

**Pull Request Title**

Add learning summary to project README

**Pull Request Description**

This Pull Request adds a My Learning section to the root README. It summarises the knowledge and practical skills gained throughout the Digital Detective assignment, including computer fundamentals, operating systems, Terminal commands, Python programming and Git version control.

**Branch Information**

| Information | Details |
|---|---|
| Base Branch | `main` |
| Compare Branch | `update-about` |
| Modified File | Root `README.md` |
| Purpose | Add a learning summary to the project documentation. |

The Pull Request should only be merged if instructed by the instructor.

**Command to Return to the Main Branch**

```bash
git switch main
```

If the Pull Request is merged, the local main branch can be updated using:

```bash
git pull origin main
```

**What Is a Branch?**

A branch is an independent line of development within a Git repository. It allows developers to make changes without directly affecting the main branch.

**What Is a Pull Request?**

A Pull Request is a request to review and merge changes from one branch into another. It allows collaborators to examine proposed changes, provide feedback and approve improvements.

**Why Are Branches and Pull Requests Useful?**

Branches allow multiple developers to work independently on different tasks. Pull Requests provide a structured way to review changes, identify mistakes, discuss improvements and maintain the quality of a shared project.

### Task 6.4 — Build Your Git Command Glossary

| Git Operation | Command | Explanation |
|---|---|---|
| Initialise a repository | `git init` | Creates a new Git repository in the current directory. |
| Check status | `git status` | Displays the current state of files and changes. |
| Stage changes | `git add .` | Stages changes within the current directory. |
| Commit changes | `git commit -m "message"` | Records staged changes with a descriptive message. |
| View history | `git log --oneline` | Displays a short version of the commit history. |
| Create a branch | `git branch branch-name` | Creates a separate branch. |
| List branches | `git branch` | Displays available local branches. |
| Switch branches | `git switch branch-name` | Changes the currently active branch. |
| Publish changes | `git push origin branch-name` | Uploads local commits to the remote repository. |
| Retrieve changes | `git pull origin branch-name` | Retrieves and integrates changes from the remote branch. |

## 3. Commands / Tools Used

| Command / Tool | Purpose |
|---|---|
| `git status` | Checks the current repository status. |
| `git add README.md` | Stages changes made to the README file. |
| `git commit -m "message"` | Records staged changes in Git history. |
| `git log --oneline` | Displays previous commits. |
| `git branch update-about` | Creates a new branch. |
| `git switch update-about` | Switches to the newly created branch. |
| `git branch` | Lists local branches and identifies the active branch. |
| `git push -u origin update-about` | Publishes the branch and establishes upstream tracking. |
| `git switch main` | Returns to the main branch. |
| `git pull origin main` | Retrieves and integrates changes from the remote main branch. |
| GitHub | Hosts repositories and supports collaboration through Pull Requests. |
| macOS Terminal (Zsh) | Provides an environment for executing Git commands. |
| Code Editor | Used for editing README files. |

## 4. My Understanding

Through this mission, I understood how Git manages project changes and how GitHub provides a platform for hosting repositories and collaborating with others.

I learned the following concepts:

1. **Version Control:** Maintains a history of changes made to project files.
2. **Staging:** Selects specific changes for inclusion in the next commit.
3. **Committing:** Records staged changes in the repository history.
4. **Pushing:** Uploads local commits to a remote repository.
5. **Pulling:** Retrieves and integrates changes from a remote repository.
6. **Branching:** Allows independent development without directly modifying the main branch.
7. **Pull Requests:** Allow proposed changes to be reviewed and discussed before merging.
8. **Meaningful Commit Messages:** Help developers understand the purpose of previous changes.

I also understood how Git and GitHub support organised project development and teamwork.

## 5. Difficulties Faced

**Difficulty 1: Understanding the Git Workflow**

Understanding the difference between staging, committing and pushing changes required additional attention.

**Difficulty 2: Understanding Branches**

It was important to understand how changes made in a separate branch remain independent of the main branch.

**Difficulty 3: Understanding Pull Requests**

Understanding the relationship between the base branch and compare branch was necessary to propose changes correctly.

## 6. How I Resolved Them

**Solution 1:**

I studied the purpose of each Git command and used `git status` and `git log --oneline` to understand how Git tracks changes.

**Solution 2:**

I explored the branch creation and switching commands to understand how separate branches allow independent development.

**Solution 3:**

I studied the Pull Request workflow and understood that the base branch receives the proposed changes, while the compare branch contains those changes.

## 7. Evidence / Files

The following files and GitHub activities are associated with this mission:

- `mission-06-git-github/README.md` — Documentation of Tasks 6.1 to 6.4.
- Root `README.md` — Project documentation and proposed My Learning section.
- `update-about` — Branch for updating the project README.
- Git commit history — Records of changes made throughout the assignment.
- Pull Request — Proposed changes from `update-about` into `main`.
- Git command glossary — Explanation of important version-control operations.

## 8. Commit Details

**Branch Commit Message:**

```text
Add learning summary to project README
```

**Mission Documentation Commit Message:**

```text
Complete Git and GitHub collaboration mission
```

The mission documentation is to be staged, committed and pushed to the main branch of the GitHub repository.