# Arithmetic Formatter

## Description
This project is part of the **Scientific Computing with Python Certification** on freeCodeCamp.  
It takes a list of arithmetic problems (addition and subtraction) and formats them vertically, similar to how you would write them on paper. Optionally, it can also display the answers.

## Features
- Supports addition (`+`) and subtraction (`-`) only.
- Handles up to 5 problems at a time.
- Automatically formats numbers with proper spacing.
- Includes error handling for:
  - Too many problems (>5)
  - Invalid operators
  - Non-digit characters
  - Numbers with more than 4 digits

## Example Usage

```python
from arithmetic_arranger import arithmetic_arranger

problems = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
formatted = arithmetic_arranger(problems, show_answers=True)
print(formatted)

## *OUTPUT*

   32      3801      45      123
+ 698    -    2    + 43    +  49
-----    ------    ----    -----
  730      3799      88      172

