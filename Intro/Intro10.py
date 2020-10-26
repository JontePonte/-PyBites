
def divide_numbers(numerator, denominator):
    """For this exercise you can assume numerator and denominator are of type
       int/str/float.
       Try to convert numerator and denominator to int types, if that raises a
       ValueError reraise it. Following do the division and return the result.
       However if denominator is 0 catch the corresponding exception Python
       throws (cannot divide by 0), and return 0"""
    
    # convert to int and rename for simple code
    try:
        num = int(numerator)
    except ValueError as error:
        raise(error)
    try:
        den = int(denominator)
    except ValueError as error:
        raise(error)

    try:
        result = num / den
    except ZeroDivisionError as error:
        return 0

    return result

print(divide_numbers("1",'0'))