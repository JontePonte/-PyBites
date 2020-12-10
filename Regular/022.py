
from functools import wraps


def make_html(func, element):         
    begin = '<' + element + '>'
    end = '<' + element + '/>'
    @wraps(func)
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs) 
  
    return begin + wrapper + end


def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper_repeat(*args, **kwargs):
            for _ in range(num_times):
                value = func(*args, **kwargs)
            return value
        return wrapper_repeat
    return decorator_repeat