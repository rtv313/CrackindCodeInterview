def valid_credit_card(card_number):
    card_number_list = list(card_number)
    card_number_list.reverse()
    sum_total = 0

    for i in range(len(card_number_list)):
        if i % 2 != 0:
            multiplication_result = int(card_number_list[i]) * 2
            if multiplication_result > 9:
                add_result = int(str(multiplication_result)[0]) + int(str(multiplication_result)[1])
                sum_total += add_result
            else:
                sum_total += multiplication_result
        else:
            sum_total += int(card_number_list[i])

    result = (sum_total % 10 == 0)

    return result


def get_card_data(card_number):
    original_card = card_number
    card_number = card_number.replace('-', '')
    if not valid_credit_card(card_number) or (not card_number.isdigit()):
        print('INVALID')
        return 'INVALID'

    if '-' in original_card:
        print('foo')

    first_pair_number = int(card_number[0] + card_number[1])

    # Visa
    if len(card_number) == 13 or len(card_number) == 16 and (
            first_pair_number not in (34, 37, 51, 52, 53, 54, 55) and int(card_number[0]) == 4):
        print('VISA')
        return 'VISA'

    # American Express
    if len(card_number) == 15 and (first_pair_number in (34, 37)):
        print('AMEX')
        return 'AMEX'

    # Master card
    if len(card_number) == 16 and first_pair_number in (51, 52, 53, 54, 55):
        print('MASTER_CARD')
        return 'MASTER_CARD'

    return 'INVALID'

# TESTING ALL CASES
#INVALID
assert get_card_data('6176292929') == 'INVALID' ,'MUST BE INVALID'

#MASTER CARD
assert get_card_data('5105105105105100') == 'MASTER_CARD','MUST BE MASTER CARD'
#MASTER CARD
assert get_card_data('5555555555554444') == 'MASTER_CARD','MUST BE MASTER CARD'

#VISA
assert get_card_data('4111111111111111') == 'VISA','MUST BE VISA'
#VISA
assert get_card_data('4012888888881881') == 'VISA','MUST BE VISA'
#VISA
assert get_card_data('4222222222222') == 'VISA','MUST BE VISA'

#AMERICAN_EXPRESS
assert get_card_data('378282246310005') == 'AMEX','MUST BE AMEX'
#AMERICAN_EXPRESS
assert get_card_data('371449635398431') == 'AMEX','MUST BE AMEX'

#WITH HYPHENS
assert get_card_data('3782-822-463-10005') == 'AMEX','MUST BE AMEX'

print('PRESS E for exit')
exit = False
while(exit==False):
    print('Number:')
    credit_card =  input()
    if(credit_card != 'E'):
        get_card_data(credit_card)
    else:
        exit = True
