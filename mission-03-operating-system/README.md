# Mission 03 — Understand Your Operating System

## 1. Task / Objective

The objective of this mission is to understand how an operating system works, explore system information, observe running processes, understand file paths and permissions, and explain the major responsibilities of an operating system.

## 2. Work Completed

### Task 3.1 — Explore Your Operating System

I used Terminal to obtain information about my computer's operating system and architecture.

**Command Used**

```bash
uname -a
```

**System Information**

| Information | Observation |
|---|---|
| Device | MacBook Pro |
| Operating System | macOS |
| Kernel Name | Darwin |
| Kernel Version | 27.2.0 |
| Processor Architecture | ARM64 |
| Processor Type | Apple Silicon |
| Shell | Zsh |

**Observation**

The command displayed information about the operating system, kernel version and processor architecture. I observed that my MacBook uses the Darwin kernel and ARM64 architecture.

### Task 3.2 — Understand Processes

A process is an instance of a program that is currently running on a computer.

**Command**

```bash
ps -ax -o pid,comm | head -n 15
```

**Explanation of the Command**

| Component | Purpose |
|---|---|
| `ps` | Displays information about running processes. |
| `-a` | Includes processes belonging to other users. |
| `-x` | Includes processes without an associated terminal. |
| `-o pid,comm` | Displays process IDs and command names. |
| `head -n 15` | Displays the first 15 lines of the output. |

**Examples of macOS System Processes**

| Process | Purpose |
|---|---|
| `launchd` | Starts and manages system services. |
| `logd` | Manages system logs. |
| `configd` | Manages system and network configuration. |
| `powerd` | Manages power-related operations. |

**Difference Between a Program and a Process**

A program is a set of instructions stored on a computer, whereas a process is an instance of a program that is currently being executed.

For example, a web browser installed on a computer is a program. When the browser is opened, it creates running processes.

The operating system manages these processes and distributes system resources among them.

### Task 3.3 — Understand File Paths and Permissions

**Absolute Path**

An absolute path specifies the complete location of a file or directory starting from the root directory.

Example:

```text
/Users/username/Desktop/digital-detective-8080
```

**Relative Path**

A relative path specifies the location of a file or directory relative to the current working directory.

Example:

```text
mission-03-operating-system/README.md
```

**Commands**

```bash
pwd
ls -l
```

The `pwd` command displays the absolute path of the current working directory.

The `ls -l` command displays detailed information about files and directories, including their permissions, ownership and sizes.

**Understanding File Permissions**

| Permission | Symbol | Meaning |
|---|---|---|
| Read | `r` | Allows reading the contents of a file. |
| Write | `w` | Allows modifying the contents of a file. |
| Execute | `x` | Allows executing a file as a program. |
| No permission | `-` | Indicates that a particular permission is not granted. |

File permissions are divided into three categories:

1. Owner
2. Group
3. Others

**Example**

```text
-rw-r--r--
```

In this example:

- The first `-` indicates a regular file.
- The owner has read and write permissions.
- The group has read permission only.
- Other users have read permission only.

File permissions help protect files from unauthorised access and modification.

### Task 3.4 — Explain Operating System Responsibilities

An operating system performs several important functions to manage computer hardware and software.

| Responsibility | Explanation | Example |
|---|---|---|
| Process Management | Manages running processes and distributes CPU time. | Running a browser and music player simultaneously. |
| Memory Management | Allocates and manages RAM for different applications. | Allocating memory when an application opens. |
| File Management | Organises, stores and retrieves files and directories. | Creating, renaming or deleting documents. |
| Device Management | Manages communication between software and hardware devices. | Using a keyboard, trackpad or printer. |
| Security and Access Control | Protects system resources and controls user access. | Password protection and file permissions. |
| User Interface | Provides an interface through which users interact with the computer. | Finder and Terminal on macOS. |

The operating system acts as an intermediary between the user, applications and computer hardware.

## 3. Commands / Tools Used

| Command / Tool | Purpose |
|---|---|
| `uname -a` | Displays operating system, kernel and architecture information. |
| `ps -ax -o pid,comm` | Displays running processes and their process IDs. |
| `head -n 15` | Limits the output to the first 15 lines. |
| `pwd` | Displays the current working directory. |
| `ls -l` | Displays detailed file information and permissions. |
| macOS Terminal (Zsh) | Used to execute system commands. |

## 4. My Understanding

Through this mission, I understood how an operating system manages computer resources and allows applications to communicate with hardware.

I learned that:

1. macOS uses the Darwin kernel.
2. ARM64 is the processor architecture used by my computer.
3. A program is a set of instructions, while a process is a running instance of a program.
4. Running processes are identified using process IDs.
5. Absolute paths specify complete file locations, while relative paths depend on the current working directory.
6. File permissions determine who can read, modify or execute files.
7. The operating system manages processes, memory, files, hardware devices and system security.

## 5. Difficulties Faced

Understanding the difference between the operating system, kernel and processor architecture required some additional explanation.

Interpreting process information and understanding the symbols used to represent file permissions were also important parts of this mission.

## 6. How I Resolved Them

I examined the output of the `uname -a` command and understood the meaning of Darwin, the kernel version and ARM64 architecture.

I studied the purpose of process IDs and the different components of the `ps` command.

I also used file permission examples to understand how read, write and execute permissions are assigned to owners, groups and other users.

## 7. Evidence / Files

- `README.md` — Documentation of Tasks 3.1 to 3.4.
- System information obtained using `uname -a`.
- Process management commands and explanations.
- Absolute and relative path examples.
- File permission examples.
- Operating system responsibilities table.

Personal system identifiers have been excluded from the documentation to maintain privacy.

## 8. Commit Details

**Suggested Commit Message:**

```text
Document operating system and file management
```

## 9. Conclusion

Mission 3 helped me understand how an operating system manages computer hardware, software and system resources.

By exploring system information and studying processes, file paths, permissions and operating system responsibilities, I gained a better understanding of how computers operate internally.