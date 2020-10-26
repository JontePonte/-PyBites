numbers = [0,1,2,3,4,5,6,7,8,345235,24,3,-56,45,75,78,46,34,-6,6,3,45,-34,534,5,-35,5,67567]


def filter_positive_even_numbers(numbers):
    """Receives a list of numbers, and returns a filtered list of only the
       numbers that are both positive and even (divisible by 2), try to use a
       list comprehension."""
    return [ num for num in numbers if num%2 == 0 if num > 0]


print(filter_positive_even_numbers(numbers))