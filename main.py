def arithmetic_arranger(problems, show_answers=False):
    # Error: Too many problems
    if len(problems) > 5:
        return "Error: Too many problems."

    # Prepare each line of output
    first_line = []
    second_line = []
    dashes = []
    answers = []

    for prob in problems:
        split = prob.split()
        if len(split) != 3:
            return "Error: Each problem must be two operands and one operator."

        left, operator, right = split

        # Error: Operator check
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        # Error: Only digits
        if not left.isdigit() or not right.isdigit():
            return "Error: Numbers must only contain digits."

        # Error: Width check
        if len(left) > 4 or len(right) > 4:
            return "Error: Numbers cannot be more than four digits."

        # Calculation
        if operator == '+':
            result = str(int(left) + int(right))
        else:
            result = str(int(left) - int(right))

        # Figure out width for this problem
        width = max(len(left), len(right)) + 2

        # Format lines
        first_line.append(left.rjust(width))
        second_line.append(operator + ' ' + right.rjust(width - 2))
        dashes.append('-' * width)
        answers.append(result.rjust(width))

    # Assemble pieces with 4 spaces between problems
    arranged = '    '.join(first_line) + '\n' + \
               '    '.join(second_line) + '\n' + \
               '    '.join(dashes)
    if show_answers:
        arranged += '\n' + '    '.join(answers)

    return arranged