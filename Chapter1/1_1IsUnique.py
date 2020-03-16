

def all_chars_unique(string):

    str_len = len(string)

    for x in range(0,str_len):

        actual_char = string[x]
        counter = 0

        for y in range(0,str_len):

            if actual_char == string[y] and actual_char != y:
                counter += 1

        if counter > 1:
            return False

    return True


print(all_chars_unique('abc'))
print(all_chars_unique('abccc'))