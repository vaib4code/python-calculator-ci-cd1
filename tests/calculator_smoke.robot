*** Settings ***
Library    Process

*** Variables ***
${PYTHON}    C:/Users/vaib0/AppData/Local/Programs/Python/Python314/python.exe

*** Test Cases ***
Verify Calculator File Exists
    ${result}=    Run Process    ${PYTHON}    --version    stdout=PIPE    stderr=PIPE
    Log    STDOUT: ${result.stdout}
    Log    STDERR: ${result.stderr}
    Should Be Equal As Integers    ${result.rc}    0

Verify Add Function Smoke Test
    ${result}=    Run Process    ${PYTHON}    -c    print(__import__('calculator').add_numbers([10,5,2]))    stdout=PIPE    stderr=PIPE
    Log    STDOUT: ${result.stdout}
    Log    STDERR: ${result.stderr}
    Should Be Equal As Integers    ${result.rc}    0
    Should Contain    ${result.stdout}    17

Verify Subtract Function Smoke Test
    ${result}=    Run Process    ${PYTHON}    -c    print(__import__('calculator').subtract_numbers([10,5,2]))    stdout=PIPE    stderr=PIPE
    Log    STDOUT: ${result.stdout}
    Log    STDERR: ${result.stderr}
    Should Be Equal As Integers    ${result.rc}    0
    Should Contain    ${result.stdout}    3

Verify Multiply Function Smoke Test
    ${result}=    Run Process    ${PYTHON}    -c    print(__import__('calculator').multiply_numbers([10,5,2]))    stdout=PIPE    stderr=PIPE
    Log    STDOUT: ${result.stdout}
    Log    STDERR: ${result.stderr}
    Should Be Equal As Integers    ${result.rc}    0
    Should Contain    ${result.stdout}    100

Verify Divide Function Smoke Test
    ${result}=    Run Process    ${PYTHON}    -c    print(__import__('calculator').divide_numbers([10,5,2]))    stdout=PIPE    stderr=PIPE
    Log    STDOUT: ${result.stdout}
    Log    STDERR: ${result.stderr}
    Should Be Equal As Integers    ${result.rc}    0
    Should Contain    ${result.stdout}    1.0

Verify Minimum Two Numbers Validation
    ${input_data}=    Set Variable    1\n2\n10\n5\nyes\nadd\n
    ${result}=    Run Process    ${PYTHON}    calculator.py    stdin=${input_data}    stdout=PIPE    stderr=PIPE
    Log    STDOUT: ${result.stdout}
    Log    STDERR: ${result.stderr}
    Should Contain    ${result.stdout}    ${ERROR_MESSAGE}
    Should Contain    ${result.stdout}    Add: 15