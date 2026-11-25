# Mission 05 — Numbers and Data

## 1. Task / Objective

The objective of this mission is to understand how computers represent numerical and textual information using binary, decimal and hexadecimal number systems.

This mission also involves verifying manual number conversions using Python, developing a simple number converter and understanding character-encoding standards such as ASCII and UTF-8.

## 2. Work Completed

### Task 5.1 — Convert Numbers by Hand

**1. Convert Decimal 13 to Binary**

| Power | 2³ | 2² | 2¹ | 2⁰ |
|---|---|---|---|---|
| Value | 8 | 4 | 2 | 1 |
| Binary Digit | 1 | 1 | 0 | 1 |

Calculation:

8 + 4 + 1 = 13

**Answer:** (13)₁₀ = (1101)₂

**2. Convert Decimal 25 to Binary**

| Power | 2⁴ | 2³ | 2² | 2¹ | 2⁰ |
|---|---|---|---|---|---|
| Value | 16 | 8 | 4 | 2 | 1 |
| Binary Digit | 1 | 1 | 0 | 0 | 1 |

Calculation:

16 + 8 + 1 = 25

**Answer:** (25)₁₀ = (11001)₂

**3. Convert Binary 1010 to Decimal**

(1010)₂ = (1 × 2³) + (0 × 2²) + (1 × 2¹) + (0 × 2⁰)

= 8 + 0 + 2 + 0

= 10

**Answer:** (1010)₂ = (10)₁₀

**4. Convert Binary 1101 to Decimal**

(1101)₂ = (1 × 2³) + (1 × 2²) + (0 × 2¹) + (1 × 2⁰)

= 8 + 4 + 0 + 1

= 13

**Answer:** (1101)₂ = (13)₁₀

**5. Convert Hexadecimal A to Decimal**

In hexadecimal, A represents the decimal value 10.

A × 16⁰ = 10 × 1 = 10

**Answer:** (A)₁₆ = (10)₁₀

**6. Convert Hexadecimal 1F to Decimal**

In hexadecimal, F represents the decimal value 15.

(1F)₁₆ = (1 × 16¹) + (15 × 16⁰)

= 16 + 15

= 31

**Answer:** (1F)₁₆ = (31)₁₀

**7. Convert Binary 1111 to Hexadecimal**

(1111)₂ = (1 × 2³) + (1 × 2²) + (1 × 2¹) + (1 × 2⁰)

= 8 + 4 + 2 + 1

= 15

The decimal value 15 is represented by F in hexadecimal.

**Answer:** (1111)₂ = (F)₁₆

### Task 5.2 — Verify Using Python

Python provides built-in functions that can be used to verify manual number conversions.

**Python Expressions and Expected Results**

| Conversion | Python Expression | Result |
|---|---|---|
| Decimal 13 to binary | `bin(13)` | `0b1101` |
| Decimal 25 to binary | `bin(25)` | `0b11001` |
| Binary 1010 to decimal | `int("1010", 2)` | `10` |
| Binary 1101 to decimal | `int("1101", 2)` | `13` |
| Hexadecimal A to decimal | `int("A", 16)` | `10` |
| Hexadecimal 1F to decimal | `int("1F", 16)` | `31` |
| Binary 1111 to hexadecimal | `hex(int("1111", 2))` | `0xf` |

**Functions Used**

- `bin()` converts an integer into its binary representation.
- `hex()` converts an integer into its hexadecimal representation.
- `int(value, base)` converts a string representing a number in a specified base into an integer.

Python uses the prefix `0b` to identify binary representations and `0x` to identify hexadecimal representations.

The expected Python results match all seven manual calculations.

### Task 5.3 — Build a Small Number Converter

**Program Description**

The Python program `number_converter.py` accepts a non-negative decimal integer from the user and converts it into binary and hexadecimal representations.

**Python Code**

```python
n = int(input("Enter a decimal number: "))

b = bin(n)
h = hex(n)

print("Binary =", b[2:])
print("Hexadecimal =", h[2:])
```

**Explanation of the Code**

1. `input()` accepts a decimal number from the user.
2. `int()` converts the entered value into an integer.
3. `bin(n)` converts the integer into its binary representation.
4. `hex(n)` converts the integer into its hexadecimal representation.
5. `[2:]` uses string slicing to remove the first two characters, which are the conversion prefixes for non-negative integers.
6. `print()` displays the converted values.

**Command to Execute the Program**

```bash
python3 number_converter.py
```

**Test Cases and Expected Results**

| Decimal Input | Binary Output | Hexadecimal Output |
|---:|---|---|
| 15 | `1111` | `f` |
| 32 | `100000` | `20` |
| 75 | `1001011` | `4b` |
| 128 | `10000000` | `80` |
| 255 | `11111111` | `ff` |

These five test cases can be used to verify whether the program correctly converts decimal numbers into binary and hexadecimal.

**What Do the Conversion Functions Do?**

The `bin()` function represents an integer using base 2, while the `hex()` function represents an integer using base 16.

Both functions return strings containing the converted representations and their respective prefixes.

### Task 5.4 — How Is Text Stored?

Computers represent text using numerical codes. Character-encoding standards provide a consistent method of storing and processing characters.

**1. Find the ASCII Decimal Codes of A and a**

Python's `ord()` function returns the Unicode code point associated with a character.

**Python Commands**

```python
ord("A")
ord("a")
ord("₹")
```

**Expected Output**

```text
65
97
8377
```

| Character | Python Expression | Unicode Code Point (Decimal) |
|---|---|---:|
| Uppercase A | `ord("A")` | 65 |
| Lowercase a | `ord("a")` | 97 |
| Indian Rupee Symbol | `ord("₹")` | 8377 |

The values 65 and 97 are also the ASCII decimal codes for uppercase A and lowercase a.

**2. Why Does a Computer Need an Encoding Standard to Store Text?**

Computers store and process information in numerical form. An encoding standard provides a consistent method of representing characters using numerical values and bytes.

Without a common encoding standard, different computers and applications might interpret the same stored data differently.

**3. Give an Example of a Character Not Included in Basic ASCII**

The Indian Rupee symbol (₹) is not included in basic ASCII.

Its Unicode code point is U+20B9, which is 8377 in decimal. It can be represented using UTF-8 encoding.

Basic ASCII supports 128 characters, whereas UTF-8 can represent the much larger Unicode character set, including characters from different languages and various symbols.

## 3. Commands / Tools Used

| Command / Tool | Purpose |
|---|---|
| `python3` | Opens the Python interactive shell. |
| `python3 number_converter.py` | Executes the number converter program. |
| `bin()` | Converts an integer into binary. |
| `hex()` | Converts an integer into hexadecimal. |
| `int()` | Converts input into an integer or interprets a number in a specified base. |
| `ord()` | Returns the Unicode code point of a character. |
| `input()` | Accepts input from the user. |
| `print()` | Displays program output. |
| `[2:]` | Removes the binary and hexadecimal prefixes for non-negative integers. |
| `exit()` | Exits the Python interactive shell. |
| Python 3.14.7 | Used for number conversions and program execution. |
| macOS Terminal (Zsh) | Used to execute Python commands. |
| Code Editor | Used to write and edit the Python program. |

## 4. My Understanding

Through this mission, I understood how computers represent numbers and text using different numerical systems and encoding standards.

The important concepts covered were:

1. Decimal is a base-10 number system.
2. Binary is a base-2 number system that uses only 0 and 1.
3. Hexadecimal is a base-16 number system that uses digits 0–9 and letters A–F.
4. Powers of the respective bases are used to perform number conversions.
5. Python provides built-in functions to simplify number-system conversions.
6. String slicing can be used to extract specific portions of a string.
7. ASCII provides numerical codes for a basic set of characters.
8. Unicode assigns code points to a much wider range of characters, and UTF-8 provides a way to encode them.
9. The `ord()` function returns the Unicode code point of a character.

This mission also demonstrates how theoretical number-system concepts can be applied through Python programming.

## 5. Difficulties Faced

**Difficulty 1: Understanding Number-System Conversions**

Converting numbers between different bases requires careful attention to place values and powers.

**Difficulty 2: Understanding Python Conversion Prefixes**

Python's binary and hexadecimal conversion functions return strings containing the prefixes `0b` and `0x`.

**Difficulty 3: Understanding Character Encoding**

Understanding the difference between ASCII, Unicode and UTF-8 required additional explanation.

## 6. How I Resolved Them

**Solution 1:**

I used place-value calculations and powers of 2 and 16 to understand number-system conversions. Python's built-in functions provide a convenient method of checking the calculations.

**Solution 2:**

I used string slicing with `[2:]` to remove the conversion prefixes and display only the binary and hexadecimal digits for non-negative integers.

**Solution 3:**

I studied the numerical representations of uppercase A, lowercase a and the Indian Rupee symbol using the `ord()` function to understand the relationship between ASCII and Unicode.

## 7. Evidence / Files

The following files and work are associated with this mission:

- `README.md` — Documentation of Tasks 5.1 to 5.4.
- `number_converter.py` — Python program for converting decimal numbers into binary and hexadecimal.
- Seven manual number-system calculations.
- Python expressions for verifying manual calculations.
- Five number converter test cases.
- ASCII and Unicode character-code examples.

**Mission Folder Structure**

```text
mission-05-numbers-data/
├── README.md
└── number_converter.py
```

## 8. Commit Details

**Commit Message:**

```text
Build number converter and practise data representation
```

The Python program and mission documentation are to be staged, committed and pushed to the GitHub repository.