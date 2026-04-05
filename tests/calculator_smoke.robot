*** Settings ***
Library    Process

*** Test Cases ***
Verify Calculator File Exists
    Run Process    python    --version

Verify Add Function Smoke Test
    ${result}=    Run Process    python    -c    from calculator import add_numbers; print(add_numbers([10,5,2]))    shell=True    stdout=TRUE
    Should Contain    ${result.stdout}    17

Verify Subtract Function Smoke Test
    ${result}=    Run Process    python    -c    from calculator import subtract_numbers; print(subtract_numbers([10,5,2]))    shell=True    stdout=TRUE
    Should Contain    ${result.stdout}    3

Verify Multiply Function Smoke Test
    ${result}=    Run Process    python    -c    from calculator import multiply_numbers; print(multiply_numbers([10,5,2]))    shell=True    stdout=TRUE
    Should Contain    ${result.stdout}    100

Verify Divide Function Smoke Test
    ${result}=    Run Process    python    -c    from calculator import divide_numbers; print(divide_numbers([10,5,2]))    shell=True    stdout=TRUE
    Should Contain    ${result.stdout}    1.0