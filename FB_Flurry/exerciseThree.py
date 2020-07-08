def verify_first_sharp(first):
    for i in range(len(first)):
        if first[i] != '#':
            return False
    return True


def first_word_is_not_sharps(first):

    if first[0] == '#':
        return False

    return True


def markdownparser(markdown):

    markdown = markdown.strip(' ')

    # Edge case
    array_words = markdown.split(' ')
    first_sharps = array_words[0]

    if first_word_is_not_sharps(first_sharps) == True:
        return markdown

    # Count html number
    count_sharps = first_sharps.count('#')

    if count_sharps > 6:
        return markdown

    if verify_first_sharp(first_sharps) == False:
        return '#NoSpace'

    result_string = ''
    for i in range(len(array_words)):
        if i != 0:
            result_string += ' ' + array_words[i]

    result_string = result_string.strip(' ')

    if count_sharps == 1:
        return '<h1>' + result_string + '</h1>'

    if count_sharps == 2:
        return '<h2>' + result_string + '</h2>'

    if count_sharps == 3:
        return '<h3>' + result_string + '</h3>'

    if count_sharps == 4:
        return '<h4>' + result_string + '</h4>'

    if count_sharps == 5:
        return '<h5>' + result_string + '</h5>'

    if count_sharps == 6:
        return '<h6>' + result_string + '</h6>'


markdownparser('### ### header')