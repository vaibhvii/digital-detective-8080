# Mission 2 — Become Comfortable with the Terminal

## 1. Task / objective

The objective of this mission was to become familiar with the Terminal and Command-Line Interface (CLI). It involved learning how to navigate directories, create and manage files, understand command flags and pipes, and explore package managers.

## 2. Work completed

### Task 2.1 — Explore basic Terminal operations

Practised basic Terminal commands to navigate directories and manage files.

| Operation | Command | What it does |
|---|---|---|
| Current-directory display | `pwd` | Displays the full path of the current working directory. |
| Directory listing | `ls` | Lists files and folders in the current directory. |
| Detailed listing | `ls -l` | Displays files with detailed information. |
| Change directory | `cd ..` | Moves to the parent directory. |
| Create directory | `mkdir` | Creates a new directory. |
| Create empty file | `touch` | Creates an empty file. |
| Copy file | `cp` | Creates a copy of an existing file. |
| Move / rename file | `mv` | Moves or renames a file. |
| Display file contents | `cat` | Displays the contents of a file. |

### Task 2.2 — Practise file changes safely

Created a directory named `terminal-practice` to practise file-management operations.

Activities performed:

- Created a text file inside the practice directory.
- Added the first line of text.
- Appended a second line without removing the first line.
- Displayed the file contents to verify both lines.
- Created a backup copy of the original file.
- Renamed the backup file.

**Concepts understood:**

1. Replacing file contents overwrites the existing content, whereas appending adds new content at the end without removing previous content.
2. Copying creates another version of a file while keeping the original. Moving changes the file's location, and renaming changes its name.
3. The `pwd` command displays the current working directory.
4. Directory listing helps identify available files and folders and makes navigation easier.

### Task 2.3 — Understand flags and pipes

**Flags**

Flags modify the behaviour of commands.

Compared the following commands:

| Command | Purpose |
|---|---|
| `ls` | Displays a normal directory listing. |
| `ls -lah` | Displays detailed information, including hidden files, with human-readable file sizes. |

The flags used are:

- `-l`: Displays detailed information.
- `-a`: Includes hidden files.
- `-h`: Displays file sizes in a human-readable format.

**Pipes**

A pipe (`|`) passes the output of one command as input to another command.

Example:

```bash
ls -lah | head
```

- `ls -lah` generates a detailed directory listing.
- `|` passes the output to the next command.
- `head` displays the first few lines of the output.

This helps combine commands and process information more efficiently.

### Task 2.4 — Understand package managers

A package manager is a tool that helps users install, update and remove software packages.

On macOS, Homebrew is a commonly used package manager.

Commands explored:

```bash
brew --version
```

Displays the installed Homebrew version.

```bash
brew list
```

Displays the packages managed by Homebrew.

**Why package managers are useful:**

Package managers make software management easier by providing a centralised way to install, update and manage applications and tools. They also help manage software dependencies and reduce the need to download and configure packages manually.

## 3. Commands / tools used

| Command / Tool | Purpose |
|---|---|
| `pwd` | Displays the current working directory. |
| `ls` | Lists directory contents. |
| `ls -l` | Displays a detailed directory listing. |
| `cd` | Changes the current directory. |
| `mkdir` | Creates directories. |
| `touch` | Creates empty files. |
| `cp` | Copies files. |
| `mv` | Moves or renames files. |
| `cat` | Displays file contents. |
| `echo` | Displays text or sends text into a file. |
| `head` | Displays the first few lines of input. |
| `brew --version` | Checks the Homebrew version. |
| `brew list` | Lists Homebrew-managed packages. |
| `>>` | Appends text to an existing file. |
| `|` | Passes the output of one command to another. |
| Terminal | Used to execute command-line instructions. |
| VS Code | Used to edit and document the mission work. |

## 4. My understanding

Through this mission, I learned how to interact with my computer using the Command-Line Interface instead of relying only on graphical applications.

I understood how directories are organised and how commands such as `pwd`, `ls` and `cd` help navigate the file system.

I also learned the difference between creating, copying, moving and renaming files. The append operator allows additional text to be added without deleting existing content.

Another important concept I learned was the use of flags. They modify commands to display information in different formats. Pipes allow multiple commands to work together by passing the output of one command to another.

Finally, I understood that package managers simplify software installation, updates and management.

## 5. Difficulties faced

- Understanding the difference between copying, moving and renaming files.
- Understanding how to append text without replacing existing content.
- Understanding the purpose of command flags.
- Understanding how pipes connect two commands.

## 6. How I resolved them

I practised the commands individually and observed their outputs in Terminal.

I compared the results of different file-management operations to understand how they affect files.

I also experimented with different command flags and used a pipe to pass directory-listing output to another command.

These practical exercises helped me understand the commands and their behaviour more clearly.

## 7. Evidence / files

- `mission-02-terminal/README.md`
- `terminal-practice/` directory.
- Text file containing two lines of text.
- Backup copy of the text file.
- Renamed backup file.
- Terminal screenshots showing command execution and outputs.
- Homebrew version and package-list output, if available.

## 8. Commit details

**Commit message:** `Complete Terminal and file management mission`

**GitHub push status:** Done 

**Repository URL:** https://github.com/vaibhvii/digital-detective-8080.git