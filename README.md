# The Digital Detective — Diwali Independent Learning Assignment

## About the Project

The Digital Detective is an independent learning assignment designed to develop an understanding of fundamental computer science concepts through theoretical learning and practical activities.

This project explores how computers work, how operating systems manage resources, how programs are executed, how data is represented, how version control supports collaboration and how computers communicate over networks.

The repository contains nine missions, each documented separately with objectives, activities, commands, observations, learning outcomes and difficulties faced.

## Assignment Information

| Information | Details |
|---|---|
| Assignment | The Digital Detective |
| Repository | digital-detective-8080 |
| Assignment Type | Diwali Independent Learning Assignment |
| Total Missions | 9 (Mission 00–08) |
| Operating System | macOS |
| Processor Architecture | ARM64 |
| Shell | Zsh |
| Programming Language | Python |
| Python Version | 3.14.7 |
| Version Control | Git |
| Repository Platform | GitHub |
| Documentation Format | Markdown |

## Mission Index

Click on any mission below to view its detailed documentation.

| Mission | Title | Topics Covered | Documentation |
|---|---|---|---|
| 00 | Create Your GitHub Workspace | Repository setup, tools and folder organisation | [View Mission 00](mission-00-setup/README.md) |
| 01 | Know Your Computer | IPOS cycle, hardware and software | [View Mission 01](mission-01-computer-basics/README.md) |
| 02 | Terminal | Commands, file management, pipes and redirection | [View Mission 02](mission-02-terminal/README.md) |
| 03 | Operating Systems | Processes, system information, paths and permissions | [View Mission 03](mission-03-operating-system/README.md) |
| 04 | Programs | Python programming, compilers and interpreters | [View Mission 04](mission-04-programs/README.md) |
| 05 | Numbers and Data | Binary, hexadecimal, ASCII, Unicode and UTF-8 | [View Mission 05](mission-05-numbers-data/README.md) |
| 06 | Git and GitHub | Version control, branches and Pull Requests | [View Mission 06](mission-06-git-github/README.md) |
| 07 | How Computers Communicate | Networking, DNS, connectivity and protocols | [View Mission 07](mission-07-networking/README.md) |
| 08 | Final Report and Submission | Repository verification and final learning outcomes | [View Mission 08](mission-08-final-report/README.md) |

## Repository Structure

```text
digital-detective-8080/
│
├── README.md
├── evidence/
│
├── mission-00-setup/
│   └── README.md
│
├── mission-01-computer-basics/
│   └── README.md
│
├── mission-02-terminal/
│   └── README.md
│
├── mission-03-operating-system/
│   └── README.md
│
├── mission-04-programs/
│   ├── README.md
│   └── hello.py
│
├── mission-05-numbers-data/
│   ├── README.md
│   └── number_converter.py
│
├── mission-06-git-github/
│   └── README.md
│
├── mission-07-networking/
│   └── README.md
│
└── mission-08-final-report/
    └── README.md
```

## Tools and Technologies Used

| Tool / Technology | Purpose |
|---|---|
| macOS | Operating system used throughout the assignment |
| Terminal | Executing commands and managing files |
| Zsh | Command-line shell |
| Python 3.14.7 | Writing programs and performing number conversions |
| Git | Tracking project changes and maintaining version history |
| GitHub | Hosting the repository and managing collaboration |
| Markdown | Creating structured project documentation |
| Code Editor | Writing and editing programs and README files |
| Ping | Testing network connectivity |
| Nslookup | Performing DNS lookups |

## How to Access and Run the Project

### Clone the Repository

The repository can be downloaded to a local computer using Git.

```bash
git clone https://github.com/vaibhvii/digital-detective-8080.git
cd digital-detective-8080
```

Python 3 must be installed to execute the Python programs.

### Program 1 — Hello from Python

**Mission:** Mission 04

**Source Code:** [hello.py](mission-04-programs/hello.py)

This program demonstrates how a simple Python instruction can be executed to display a message.

Run the following command from the root repository directory:

```bash
python3 mission-04-programs/hello.py
```

**Output:**

```text
Hello from Python
```

### Program 2 — Number Converter

**Mission:** Mission 05

**Source Code:** [number_converter.py](mission-05-numbers-data/number_converter.py)

This program accepts a non-negative decimal integer and converts it into binary and hexadecimal representations.

Run the following command from the root repository directory:

```bash
python3 mission-05-numbers-data/number_converter.py
```

**Example Input and Expected Output:**

```text
Enter a decimal number: 75
Binary = 1001011
Hexadecimal = 4b
```

The program uses Python's built-in `bin()` and `hex()` functions along with string slicing to remove conversion prefixes.

## Practical Activities Performed

Throughout the assignment, the following practical activities were covered:

- Creating and organising a GitHub repository.
- Navigating directories using Terminal commands.
- Creating, copying, moving and managing files.
- Understanding command flags, pipes and redirection.
- Exploring operating-system and processor architecture information.
- Studying running processes and file permissions.
- Writing and executing Python programs.
- Converting numbers between decimal, binary and hexadecimal.
- Exploring ASCII and Unicode character codes using Python.
- Staging, committing and pushing project changes.
- Creating branches and working with Pull Requests.
- Performing network connectivity tests and DNS lookups.
- Reviewing and organising project documentation.

## Selected Practical Results

| Activity | Result |
|---|---|
| Operating System Kernel | Darwin |
| Kernel Version | 27.2.0 |
| Processor Architecture | ARM64 |
| Python Version | 3.14.7 |
| Hello Python Program | Executed successfully |
| Network Connectivity Test | Successful |
| Ping Packets Transmitted | 4 |
| Ping Packets Received | 4 |
| Packet Loss | 0.0% |
| Average Round-Trip Response Time | 6.233 ms |
| DNS Lookup | Successful |

Detailed explanations and observations are available in the respective mission README files.

## Documentation Format

Each mission README follows a consistent eight-section format:

1. Task / Objective
2. Work Completed
3. Commands / Tools Used
4. My Understanding
5. Difficulties Faced
6. How I Resolved Them
7. Evidence / Files
8. Commit Details

This structure makes it easier to understand the activities performed, the concepts learned and the practical work associated with each mission.

## Git and GitHub Workflow

Git was used throughout the assignment to maintain a record of project changes.

The basic workflow followed was:

```bash
git status
git add filename
git commit -m "Descriptive commit message"
git push origin main
```

Meaningful commit messages were used to describe the work associated with different missions.

A separate branch named `update-about` was also used for the learning-summary activity in Mission 06.

This activity demonstrates how branches and Pull Requests allow changes to be proposed and reviewed without directly modifying the main branch.

## Challenges and Problem-Solving

During the assignment, I explored several concepts that required additional understanding and practical experience.

One challenge was understanding the difference between staging, committing and pushing changes in Git.

I also encountered a Git push rejection because the remote repository contained changes that were not available locally.

I resolved this issue using:

```bash
git pull --rebase origin main
git push origin main
```

This helped me understand the importance of keeping local and remote repositories synchronised.

Other challenges included understanding file permissions, number-system conversions, Python conversion prefixes and network command outputs.

These concepts were explored through practical commands, examples and theoretical explanations.

## My Learning

### Computer Fundamentals

I understood how hardware and software work together and how the Input-Process-Output-Storage cycle explains the basic functioning of computers.

### Terminal and Operating Systems

I developed practical knowledge of command-line operations, directory navigation, file management, running processes, system resources and file permissions.

### Python Programming

I learned how to create and execute Python programs, accept user input, use built-in functions and understand the difference between compilers and interpreters.

### Numbers and Data Representation

I understood how computers represent numerical information using binary and hexadecimal systems. I also learned about ASCII, Unicode and UTF-8 encoding.

### Git and GitHub

I learned how version control helps maintain project history, track changes and support collaboration through branches and Pull Requests.

### Computer Networking

I understood different network types, the role of DNS and routers, communication protocols, packet switching and the client-server model.

I also gained practical experience in testing network connectivity and performing DNS lookups.

### Documentation and Project Management

I learned how to organise a project into separate directories, prepare structured Markdown documentation, maintain meaningful commit messages and publish work through GitHub.

## Security and Privacy

The repository is intended for academic learning and evaluation.

The following information should not be included in public project documentation:

- Passwords and authentication credentials.
- GitHub personal access tokens.
- Private network information.
- Device serial numbers and hardware identifiers.
- Unnecessary personal information.

Selected command outputs are included in mission documentation where appropriate.

## Assignment Completion Status

| Mission | Status |
|---|---|
| Mission 00 — GitHub Workspace | Completed |
| Mission 01 — Computer Basics | Completed |
| Mission 02 — Terminal | Completed |
| Mission 03 — Operating Systems | Completed |
| Mission 04 — Programs | Completed |
| Mission 05 — Numbers and Data | Completed |
| Mission 06 — Git and GitHub | Completed |
| Mission 07 — Networking | Completed |
| Mission 08 — Final Report | Completed |

## Final Repository Link

[Digital Detective — GitHub Repository](https://github.com/vaibhvii/digital-detective-8080)

## Conclusion

The Digital Detective assignment provided an opportunity to explore fundamental computer science concepts through a combination of theoretical learning and practical activities.

Through this assignment, I gained experience in using Terminal, understanding operating systems, writing Python programs, representing data, managing repositories with Git and exploring computer networking.

The assignment also helped me develop problem-solving, technical documentation and project organisation skills that will be useful in future computer science projects.