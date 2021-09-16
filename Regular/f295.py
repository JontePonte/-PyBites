
"""
Write a function that accepts a list of lists and joins them with a separator character, therefore flattening and separating.  

Examples:  

>>> join_lists([ ['a', 'b'], ['c'] ], '&')
['a', 'b', '&', 'c']
>>> join_lists([ ['a', 'b'], ['c'], ['d', 'e'] ], '+')
['a', 'b', '+', 'c', '+', 'd', 'e']
"""



from typing import List, Union


def join_lists(lst_of_lst: List[List[str]], sep: str) -> Union[List[str], None]:
    if not lst_of_lst:
        return None
    
    lists_separator = []
    lists_separator.append(lst_of_lst[0])
    for lst in lst_of_lst[1:]:
        lists_separator.append([sep])
        lists_separator.append(lst)

    single_list = []
    for lst in lists_separator:
        single_list += lst

    return single_list



print(join_lists([ ['a', 'b'], ['c'] ], '&'))
print(join_lists([ ['a', 'b'], ['c'], ['d', 'e'] ], '+'))
