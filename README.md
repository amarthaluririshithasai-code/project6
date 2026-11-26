# Project 6 – Password Policy Validation Engine

## Description
The Password Policy Validation Engine is a Python program designed to check whether a password satisfies a set of security requirements. It validates the password based on its length, uppercase letters, lowercase letters, digits, special characters, and repeated characters.

## Objectives
- To validate passwords using Python.
- To check uppercase and lowercase letters.
- To identify digits and special characters.
- To check password length.
- To apply conditional statements and string operations.

## Concepts Used
- Variables and Data Types
- Strings and String Methods
- Conditional Statements
- Loops
- Logical Operators

## Assumptions
- Minimum password length is 8 characters.
- At least one uppercase letter is required.
- At least one lowercase letter is required.
- At least one digit is required.
- At least one special character is required.
- Three or more consecutive identical characters are not allowed.
- The word "password" is not allowed.

## Sample Output

**Example 1:**
```text
Enter password: Hello@123
Password is Valid.
```

**Example 2:**
```text
Enter password: hello123
Password is Invalid.
Reasons:
- Uppercase letter is missing.
- Special character is missing.
```

**Example 3:**
```text
Enter password: Passsword@123
Password is Invalid.
Reasons:
- The word 'password' is not allowed.
- Three consecutive identical characters are not allowed.
```

## How to Run
1. Open the project folder in Visual Studio Code.
2. Open the `main.py` file.
3. Run the Python program.
4. Enter a password when prompted.
5. Check the validation result.

## Conclusion
This project demonstrates how Python strings, loops, conditional statements, and logical operators can be used to validate passwords based on predefined rules.
