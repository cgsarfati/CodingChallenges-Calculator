"""Calculator

    >>> calc("+ 1 2")  # 1 + 2
    3

    >>> calc("* 2 + 1 2")  # 2 * (1 + 2)
    6

    >>> calc("+ 9 * 2 3")   # 9 + (2 * 3)
    15

Let's make sure we have non-commutative operators working:

    >>> calc("- 1 2")  # 1 - 2
    -1

    >>> calc("- 9 * 2 3")  # 9 - (2 * 3)
    3

    >>> calc("/ 6 - 4 2")  # 6 / (4 - 2)
    3
"""


def calc(s):
    """Evaluate expression."""

    # + 1 2 --> move operator one over --> 1 + 2
        # need to store #s to var, then put operator b/w them
    # considerations: only need .pop action --> implement Stack

    # str to lst
    values = s.split()

    # store right-most num
    operand2 = int(values.pop())

    # loop until expression finished
    while values:

        # store remaining num for current math
        operand1 = int(values.pop())

        # store operator
        operator = values.pop()

        # do math, then update "right hand" value for next time we do math
        if operator == "+":
            operand2 = operand1 + operand2

        elif operator == "-":
            operand2 = operand1 - operand2

        elif operator == "*":
            operand2 = operand1 * operand2

        elif operator == "/":
            operand2 = operand1 / operand2

    # return final result
    return operand2

# ALTERNATIVE SOLN - RECURSION?
    # could switch 1st & 2nd items, store somewhere, then slice. repeat.
    # e.g. [- 9 * 2 3] --> [9 - * 2 3] --> [9 -] [* 2 3]
            # [9 - ] [2 * 3] --> [9 - 2 *] [3] --> [9 - 2 * 3] --> 9-2*3


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED; WELL-CALCULATED! ***\n"
