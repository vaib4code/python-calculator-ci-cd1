# Python Calculator CI/CD Project

## Overview
This project is a simple command-line calculator application built in Python. It is being developed in multiple iterations and will be integrated with Jenkins for CI/CD and Robot Framework for automated testing.

## Tools and Technologies
- Python
- PyCharm
- GitHub
- Jenkins
- Robot Framework

## Project Goal
The goal of this project is to:
- build a simple Python calculator application
- manage the code using GitHub
- use Jenkins to automate build and test execution
- trigger Robot Framework smoke tests whenever a new version is pushed

## Current Version
### Iteration 1
This version supports basic calculator operations on integers:
- Add
- Subtract
- Multiply
- Divide

## Application Flow
1. The program asks the user how many integers they want to enter.
2. The user enters two or more integers.
3. The program asks whether the user wants to perform a specific function.
4. If the user selects **yes**, they choose one function:
   - add
   - subtract
   - multiply
   - divide
5. If the user selects **no**, the program performs all four functions.
6. The result or results are displayed in the command line.

## Example
### Specific function
```text
How many integers do you want to enter? 3
Enter integer 1: 10
Enter integer 2: 5
Enter integer 3: 2
Do you want to perform a specific function? (yes/no): yes
Which function do you want? (add/subtract/multiply/divide): add
Add: 17
