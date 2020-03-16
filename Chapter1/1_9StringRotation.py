
def string_is_rotation(s1,s2):

    if len(s1) != len(s2):
        return False

    s1 = s1 + s1

    if s2 in s1:
        return True
    return False


print('waterbottle, erbottlewat:'+str(string_is_rotation('waterbottle','erbottlewat')))

