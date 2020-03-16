
def check_palindrome_permutation(string):
    #aabaa
    #aabbbaa
    #aacbbcaa
    #aaaa
    # All are pairs
    # All pairs minus one  if more than one impair is not palindrome
    char_counter = dict()

    for char in string:

        if char in char_counter:
            char_counter[char]+= 1
        else:
            char_counter[char] = 1

    count_not_pairs = 0

    for key in char_counter.keys():

        if char_counter[key]%2 != 0:
            count_not_pairs+=1

    if count_not_pairs > 1:
        print(string+':'+'Not palindrome')
        return

    print(string+':'+'Is palindrome')

#aabaa
#aabbbaa
#aacbbcaa
#aaaa
check_palindrome_permutation('aabaa')
check_palindrome_permutation('aabbbaa')
check_palindrome_permutation('aacbbcaa')
check_palindrome_permutation('aaaa')
check_palindrome_permutation('aaaabbbz')
check_palindrome_permutation('aaaabbbcz')