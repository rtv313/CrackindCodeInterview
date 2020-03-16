

def check_permutation(string_one,string_two):


    if len(string_one) != len(string_two):
        return False

    dict_one = dict()
    dict_two = dict()

    set_one =  set()
    set_two =  set()


    for char in string_one:

        set_one.add(char)
        if char in dict_one:
            dict_one[char]+=1
        else:
            dict_one[char]=1

    for char in string_two:
        set_two.add(char)
        if char in dict_two:
            dict_two[char] += 1
        else:
            dict_two[char] = 1

    if set_one != set_two:
        return False

    for key in dict_one.keys():
        if dict_one[key] != dict_two[key]:
            return False

    return True


    return True

print(check_permutation('dog','god'))
print(check_permutation('dog','godd'))
print(check_permutation('aabbccc','cccbbaa'))
print(check_permutation('aabbccc','cccbtaa'))
