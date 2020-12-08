
test1 = ['A', 'f', '.', 'Q', 2]  # returns index 2 (dot is non-alphanumeric among alphanumerics)
test2 = ['.', '{', ' ^', '%', 'a']  # returns index 4 ('a' is alphanumeric among non-alphanumerics)

def get_index_different_char(chars):
    is_alnum = []
    no_alnum = []
    for index, char in enumerate(chars):
        if str(char).isalnum():
            is_alnum.append([char, index])
        else:
            no_alnum.append([char,index])
    
    if len(is_alnum) == 1:
        output = is_alnum[0][1]
    elif len(no_alnum) == 1:
        output = no_alnum[0][1]
    else:
        output = "No single alphanumeric or non-alphanumeric elements"
    return output


print(get_index_different_char(test2))
