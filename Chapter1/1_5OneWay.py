# One Away: There are three types of edits that can be performed on strings:
# insert a character, remove a character, or replace a character.
# Given two strings, write a function to check if they are one edit (or zero edits) away

def check_lens(str_one, str_two):
    if len(str_one) == len(str_two):
        return 0

    if len(str_one) > len(str_two):
        return 1

    return 2


def create_dic_set(string):
    dictionary = dict()
    set_chars = set()
    for char in string:
        set_chars.add(char)
        if char in dictionary:
            dictionary[char] += 1
        else:
            dictionary[char] = 1

    return dictionary, set_chars


def one_way(str_one, str_two):
    type_edit = check_lens(str_one, str_two)
    dict_one, set_one = create_dic_set(str_one)
    dict_two, set_two = create_dic_set(str_two)

    if type_edit == 0:  # No add or delete

        dif_set_one = set_one.difference(set_two)
        dif_set_two = set_two.difference(set_one)
        full_join_sets = dif_set_one.union(dif_set_two)

        dif_set_len = len(full_join_sets)
        if dif_set_len > 1:
            return False

        if set_one == set_two:
            for key in dict_one.keys():
                if dict_two[key] - dict_one[key] > 1:
                    return False

        return True

    if type_edit == 1:  # Delete
        if len(str_one) - len(str_two) > 1:
            return False
        else:
            dif_set_one = set_one.difference(set_two)
            dif_set_two = set_two.difference(set_one)
            full_join_sets = dif_set_one.union(dif_set_two)

            dif_set_len = len(full_join_sets)
            if len(dif_set_one) > 0:
                return True
            elif dif_set_len > 0:
                return False

            if set_one == set_two:
                for key in dict_one.keys():
                    if dict_two[key] - dict_one[key] >= 1:
                        return False

            return True

    if type_edit == 2:  # Add

        if len(str_two) - len(str_one) > 1:
            return False
        else:
            for key in dict_one.keys():
                if dict_two[key] - dict_one[key] > 1:
                    return False

            return True


print('aabbcc -> aabbcd ' + str(one_way('aabbcc', 'aabbcd')) + ':' + 'True')
print('aabbcc -> aabbdd ' + str(one_way('aabbcc', 'aabbdd')) + ':' + 'False')
print('ababab -> abbbbb ' + str(one_way('ababab', 'abbbbb')) + ':' + 'False')
print('ababab -> ababbb ' + str(one_way('ababab', 'ababbb')) + ':' + 'True')
print('ababab -> bbabbb' + str(one_way('ababab', 'bbabbb')) + ':' + 'False')

print('aabbcc -> aabbc ' + str(one_way('aabbcc', 'aabbc')) + ':' + 'True')
print('aabbcc -> abbbc ' + str(one_way('aabbcc', 'abbbc')) + ':' + 'False')
print('aabbcc -> axbbc ' + str(one_way('aabbcc', 'axbbc')) + ':' + 'False')
print('aabbc -> aabb ' + str(one_way('aabbc', 'aabb')) + ':' + 'True')

print('aabbcc -> aabbccd ' + str(one_way('aabbcc', 'aabbccd')) + ':' + 'True')
print('aabbcc -> aabbcxcd ' + str(one_way('aabbcc', 'aabbcxcd')) + ':' + 'False')
print('aabbcc -> aabbccc ' + str(one_way('aabbcc', 'aabbccc')) + ':' + 'True')
