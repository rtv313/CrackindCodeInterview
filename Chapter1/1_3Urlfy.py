# Instantiate the string

def easy_urlfy(string):
    # Trim the given string
    s = string.strip()
    # Replace All space (unicode is \\s) to %20
    s = s.replace(' ', "%20")
    return s


print(easy_urlfy("Mr John Smith "))


def urlify(in_string, in_string_length):
    return ''.join('%20' if c == ' ' else c for c in in_string[:in_string_length])


print(urlify("Mr John Smith", 30))


def urlify_scratch(string):
    string = string.strip()
    spaces_count = string.count(' ')
    total_new_spaces = spaces_count * 2
    last_pos_original = len(string) - 1
    str_list = list(string)

    # Add extra spaces
    for space in range(total_new_spaces):
        str_list.append(' ')

    last_pos_relative = last_pos_original

    for r_index in range(last_pos_original, 0, -1):  # From back to beginning

        if str_list[r_index] == ' ':
            # from last char to actual index
            iter_times = last_pos_relative - r_index

            for index in range(0, iter_times):
                temp = str_list[last_pos_relative - index]
                str_list[last_pos_relative - index + 2] = temp

            str_list[r_index] = '%'
            str_list[r_index + 1] = '2'
            str_list[r_index + 2] = '0'

            last_pos_relative += 2

    return ''.join(str_list)


print(urlify_scratch("Mr John Smith"))
