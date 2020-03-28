"""
Implement the vowel_count function so that it returns the number of English-language vowels in a string.
"""

def vowel_optimized(input_string):

    sum_vowels = 0
    input_string = input_string.lower()

    sum_vowels += input_string.count('a')
    sum_vowels += input_string.count('e')
    sum_vowels += input_string.count('i')
    sum_vowels += input_string.count('o')
    sum_vowels += input_string.count('u')

    return sum_vowels


def vowel_count(input_string):
    """
    Returns the number of vowels (a, e, i, o, u) in a string.

    Example:
    >>> vowel_count('I wonder how many vowels?')
    7
    """
    input_string = input_string.lower()
    vowels = ('a', 'e', 'i', 'o', 'u')
    sum_total = 0

    for x in input_string:

        if x in vowels:
            sum_total += 1

    return sum_total


# DO NOT MODIFY BELOW THIS LINE!

def test_equal(x, y):
    if x == y:
        print('PASSED!!')
    else:
        print('Expected `{}` to equal `{}`'.format(x, y))


test_equal(vowel_optimized('Ethan loves cheese'), 7)
test_equal(vowel_optimized('Ethan does NOT love cheese'), 10)
test_equal(vowel_optimized(''), 0)
