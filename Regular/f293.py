"""
Write a function that accepts a list of numbers and converts them into n digit integers.

Examples:  

n_digit_numbers([1, 2, 3], 2)  => [10, 20, 30]

n_digit_numbers([8, 9, 10], 2)  => [80, 90, 10]

n_digit_numbers([-1.1, 2.22, -3.333], 3)  => [-110, 220, -333]
Note: Negative numbers should keep their negativity and calling the function with n < 1 should raise a

"""


from typing import List, TypeVar

T = TypeVar("T", int, float)


def n_digit_numbers(numbers: List[T], n: int) -> List[int]:
    if n < 1:
        raise ValueError

    output = []
    for number in numbers:
        str_num = str(number)
        neg = False
        # Check negativity
        if str_num[0] == '-':
            neg = True
            str_num = str_num[1:]

        # Separate numbers and remove decimal sign
        str_list = [char for char in str_num if not char == '.']

        # Make correct length and pad zeros
        if len(str_list) == n:
            str_correct = str_list
        elif len(str_list) > n:
            str_correct = str_list[:n]
        else:
            str_correct = str_list + ['0']*(n - len(str_list))
        
        # Combine string
        output_positive = ''
        for char in str_correct:
            output_positive += char
        
        # Make int again and fix negativity
        output_element = int(output_positive)
        if neg:
            output_element *= -1

        output.append(output_element)
    return output


print(n_digit_numbers([1, 2, 3], 2))
print(n_digit_numbers([8, 9, 10], 2))
print(n_digit_numbers([-1.1, 2.22, -3.333], 3))
