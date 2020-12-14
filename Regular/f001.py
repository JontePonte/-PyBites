

def sum_numbers(numbers=None):
    # Check and fix input
    if numbers == None:
        numbers = range(1,101)
    
    return sum(num for num in numbers)