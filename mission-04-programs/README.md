# Mission 04 — Understand Programs

## 1. Task / Objective

The objective of this mission is to understand how computer programs work, write and execute a simple Python program, and understand the difference between compilers and interpreters.

## 2. Work Completed

### Task 4.1 — Write and Run a Python Program

I created a Python file named `hello.py` inside the `mission-04-programs` directory.

**Python Code**

```python
print("Hello from Python")
```

The `print()` function displays the specified message on the screen.

**Command Used**

```bash
python3 hello.py
```

**Output**

```text
Hello from Python
```

The program executed successfully and displayed the expected message without any errors.

**Checking the Python Version**

```bash
python3 --version
```

**Output**

```text
Python 3.14.7
```

**Observations**

| Information | Result |
|---|---|
| Programming Language | Python |
| Python Version | 3.14.7 |
| File Name | hello.py |
| Execution Environment | macOS Terminal |
| Program Output | Hello from Python |
| Execution Status | Successful |

### Task 4.2 — Understand Compilers and Interpreters

Computers require instructions in a form that they can execute. Compilers and interpreters help translate and execute programs written in programming languages.

**What Is a Compiler?**

A compiler translates source code into another form, such as machine code, before execution.

The compiled program can then be executed by the computer.

Examples of commonly compiled languages include C and C++.

**What Is an Interpreter?**

An interpreter executes program instructions at runtime. It allows programmers to run their code without manually creating a separate executable file beforehand.

Python and Ruby are commonly associated with interpreted execution.

**Difference Between Compilers and Interpreters**

| Feature | Compiler | Interpreter |
|---|---|---|
| Translation | Translates source code before execution. | Processes and executes code at runtime. |
| Execution | Executes the compiled program. | Executes code through an interpreter. |
| Error Detection | Many errors are detected during compilation. | Some errors are detected during execution. |
| Execution Speed | Generally faster after compilation. | May be slower due to runtime overhead. |
| Output | May generate a separate executable file. | Usually does not require a separate executable file. |
| Examples | C and C++ | Python and Ruby |

**How Does Python Execute a Program?**

Python typically converts source code into an intermediate representation called bytecode. The Python Virtual Machine then executes this bytecode.

When I executed `python3 hello.py`, Python processed the instructions written in the file and displayed the specified message in Terminal.

## 3. Commands / Tools Used

| Command / Tool | Purpose |
|---|---|
| `cd mission-04-programs` | Navigates to the Mission 04 directory. |
| `touch hello.py` | Creates the Python program file. |
| `python3 hello.py` | Executes the Python program. |
| `python3 --version` | Displays the installed Python version. |
| `print()` | Displays a message or value on the screen. |
| Python 3.14.7 | Used to execute the Python program. |
| macOS Terminal (Zsh) | Used to run commands and observe program output. |
| Code Editor | Used to write and edit the Python program. |

## 4. My Understanding

Through this mission, I understood how computer programs contain instructions that tell a computer what to do.

I learned that:

1. A program is a collection of instructions written to perform a particular task.
2. Source code contains instructions written using a programming language.
3. Python programs can be stored in files with the `.py` extension.
4. The `print()` function displays information on the screen.
5. Python programs can be executed directly from Terminal using the `python3` command.
6. Compilers and interpreters use different approaches to translating and executing programs.
7. Python typically uses bytecode and a virtual machine to execute instructions.

I also understood the relationship between source code, programming languages and program execution.

## 5. Difficulties Faced

No execution errors were encountered while running the Python program.

Understanding the difference between compilation and interpretation required additional theoretical explanation.

## 6. How I Resolved Them

I compared compilers and interpreters based on their translation methods, execution processes, error detection and examples.

I also studied how Python executes source code through bytecode and the Python Virtual Machine.

I verified the successful execution of my program by comparing the actual Terminal output with the expected output.

## 7. Evidence / Files

The following files and outputs are associated with this mission:

- `README.md` — Documentation of Tasks 4.1 and 4.2.
- `hello.py` — Python program displaying a simple message.
- Successful program execution output: `Hello from Python`.
- Python version verification: `Python 3.14.7`.
- Comparison table explaining compilers and interpreters.

**Mission Folder Structure**

```text
mission-04-programs/
├── README.md
└── hello.py
```

## 8. Commit Details

**Commit Message:**

```text
Compare compilers and interpreters
```

The Python program and mission documentation are to be staged, committed and pushed to the GitHub repository.