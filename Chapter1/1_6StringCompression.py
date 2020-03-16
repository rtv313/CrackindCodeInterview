#String Compression: Implement a method to perform basic string compression using the counts of repeated characters.
#For example, the string aabcccccaaa would become a2blc5a3.
#If the "compressed "string would not become smaller than the original string, your method should return the original string.
#You can assume the string has only uppercase and lowercase letters (a - z)

def compress_string(string):

    actual_char = string[0]
    counter = 0
    result=''
    only_one_list = []

    for char in string:

        if char == actual_char:
            counter+=1
        else:
            result+=actual_char+str(counter)
            actual_char=char

            if counter == 1:
                only_one_list.append(1)
            else:
                only_one_list.append(0)

            counter=1

    result += actual_char + str(counter)

    for x in only_one_list:
        if x != 1:
            return result

    return string

print(compress_string('aabcccccaaa')+'->'+'a2b1c5a3')
print(compress_string('abcd')+'->'+'abcd')
