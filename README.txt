Python Calculator CI/CD Project
Overview
This project is a simple command-line calculator application developed in Python. It is being built as a learning project to demonstrate Python development, GitHub version control, Jenkins CI/CD integration, and Robot Framework automation testing.

Technology Stack
Python
PyCharm
GitHub
Jenkins
Robot Framework
Features
Iteration 1
The current version supports basic integer operations:

Addition
Subtraction
Multiplication
Division
Application Workflow
The user is prompted to enter how many integers they want to use.
The user enters two or more integers.
The application asks whether the user wants to perform a specific function.
If the user selects yes, they can choose one of the following operations:
add
subtract
multiply
divide
If the user selects no, the application performs all four operations.
The results are displayed in the command line.
Example Output
If the user chooses a specific function, the application displays the result for that function only.

If the user chooses not to specify a function, the application displays all results in the following format:

Add: result
Subtract: result
Multiply: result
Divide: result

Future Enhancements
Iteration 2
Add trigonometric functions
Add logarithmic functions
Iteration 3
Add float support
Improve validation and error handling
CI/CD Plan
This project is intended to follow a simple CI/CD workflow:

Code is written and updated in PyCharm
Changes are pushed to GitHub
Jenkins pulls the latest version of the code
Robot Framework smoke tests are triggered automatically
Jenkins reports build and test status
Project Structure
calculator.py — main application file
tests/ — automation test folder
README.md — project documentation
Objective
The objective of this project is to build a simple Python application in multiple iterations while integrating source control, automated testing, and CI/CD practices.