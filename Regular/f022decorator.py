
from functools import wraps


# def make_html(func, element):         
#     begin = '<' + element + '>'
#     end = '<' + element + '/>'
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         func(*args, **kwargs)
#         return func(*args, **kwargs) 
  
#     return begin + wrapper + end


def make_html(element):
    def decorator_html(func):
        @wraps(func)
        def wrapper_html(*args, **kwargs):
            before = '<' + element + '>'
            func_value = func(*args, **kwargs) 
            after = '</' + element + '>'
            return before + func_value + after
        return wrapper_html
    return decorator_html
