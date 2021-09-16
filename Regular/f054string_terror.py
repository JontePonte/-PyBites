
""""
In this Bite you complete print_hanging_indents to print a poem (or text) in a nicer way.

For example calling it on (part of) Christina Rosetti's Remember it should convert:

                      Remember me when I am gone away,
                      Gone far away into the silent land;
                      When you can no more hold me by the hand,

                      Nor I half turn to go yet turning stay.

                      Remember me when no more day by day
                      You tell me of our future that you planned:
                      Only remember me; you understand
to:
Remember me when I am gone away,
    Gone far away into the silent land;
    When you can no more hold me by the hand,
Nor I half turn to go yet turning stay.
Remember me when no more day by day
    You tell me of our future that you planned:
    Only remember me; you understand


print the resulting poem (don't return it)! The tests include another text snippet from Shakespeare. Have fun!
"""


INDENTS = 4


def print_hanging_indents(poem):
    poem_list = poem.strip().strip('\n').split('\n')
    poem_list_formated = [line.strip() for line in poem_list]

    poem_output = poem_list_formated[0]
    for index, line in enumerate(poem_list_formated[1:],1):
        if line != '':
            poem_output += '\n'
        if poem_list_formated[index-1] != '' and line != '':
            poem_output += ' '*INDENTS + line
        else:
            poem_output += line

    print(poem_output)


poem = """Remember me when I am gone away,
Gone far away into the silent land;
When you can no more hold me by the hand,

Nor I half turn to go yet turning stay.

Remember me when no more day by day
You tell me of our future that you planned:
Only remember me; you understand"""


shakespeare_unformatted = """
                          To be, or not to be, that is the question:
                          Whether 'tis nobler in the mind to suffer

                          The slings and arrows of outrageous fortune,
                          Or to take Arms against a Sea of troubles,
                          """

print_hanging_indents(shakespeare_unformatted)
