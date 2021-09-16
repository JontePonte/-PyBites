
"""
Designer Mary wants to convert her CSS from statements like background-color: rgb(128, 128, 0); to: background-color: #808000;.

Don't worry, you don't have to rewrite CSS, just complete the rgb_to_hex helper for her that takes a tuple of RGB (3 ints) 
and converts it to the corresponding hex value.

For example for Maroon you would call it like rgb_to_hex((128, 0, 0)) and it would return the hex #800000.
Make sure you check that each r, g and b int is within the valid range of 0 and 255 (both included), 
if not raise a ValueError, Explicit is better than implicit (Zen).

Check the TESTS tab for more examples, there we check your code for 16 colors and 3 excepions. Have fun!
"""


def rgb_to_hex(rgb):
    """Receives (r, g, b)  tuple, checks if each rgb int is within RGB
       boundaries (0, 255) and returns its converted hex, for example:
       Silver: input tuple = (192,192,192) -> output hex str = #C0C0C0"""
    for num in rgb:
        if num < 0 or num > 255:
            raise ValueError
    
    hex_values = [hex(num)[2:].upper() for num in rgb]

    hex_padded = []
    for value in hex_values:
        if len(value) == 1:
            hex_padded.append('0' + str(value))
        else:
            hex_padded.append(str(value))

    return '#'+''.join(hex_padded)


col = (120, 245, 3)
print(rgb_to_hex(col))
