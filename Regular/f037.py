
"""
Although you have to be careful using recursion it is one of those concepts you want to at least understand. It's also commonly used in coding interviews :)

In this beginner Bite we let you rewrite a simple countdown for loop using recursion. See countdown_for below, it produces the following output:
"""


def countdown_for(start=10):
    for i in reversed(range(1, start + 1)):
        print(i)
    print('time is up')


def countdown_recursive(start=10):
    value = start
    print(value)
    if value > 1:
        countdown_recursive(start=value-1)
    else:
        print('time is up')


countdown_recursive(30)
