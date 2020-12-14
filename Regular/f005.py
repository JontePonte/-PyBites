NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']



'''
In this bite you will work with a list of names.

First you will write a function to take out duplicates and title case them.

Then you will sort the list in alphabetical descending order by surname and lastly determine what the shortest first name is. For this exercise you can assume there is always one name and one surname.

With some handy Python builtins you can write this in a pretty concise way. Get it sorted :)
'''


def dedup_and_title_case_names(names):
    """Should return a list of title cased names,
       each name appears only once"""
    return list({name.title() for name in names})


def sort_by_surname_desc(names):
    """Returns names list sorted desc by surname"""
    # clean data and put surenames first
    names = dedup_and_title_case_names(names)
    names_reordered = change_name_order(names)

    # sort (by surename) and put first name first name first
    names_reordered_sorted = sorted(names_reordered, reverse=True)
    names_sorted = change_name_order(names_reordered_sorted)

    return names_sorted


def shortest_first_name(names):
    """Returns the shortest first name (str).
       You can assume there is only one shortest name.
    """
    names = dedup_and_title_case_names(names)
    names_first = [name.split()[0] for name in names]
    names_last = [name.split()[1] for name in names]

    names_length_in_front = [" ".join([str(len(first)), first,last]) for first, last in zip(names_first,names_last)]
    names_length_in_front_sorted = sorted(names_length_in_front)
    
    names_sorted_first = [name.split()[1] for name in names_length_in_front_sorted]
    names_sorted_last = [name.split()[2] for name in names_length_in_front_sorted]
    
    names_sorted = [" ".join([first, last]) for first, last in zip(names_sorted_first, names_sorted_last)]

    return names_sorted[0].split()[0]

def change_name_order(names):
    """ Change order of first and lanst name """
    names_first = [name.split()[0] for name in names]
    names_last = [name.split()[1] for name in names]
    names_reordered = [' '.join([last, first]) for last, first in zip(names_last, names_first)]

    return names_reordered


# print(dedup_and_title_case_names(NAMES))
print(sort_by_surname_desc(NAMES))
print(shortest_first_name(NAMES))
