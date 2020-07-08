def solution(number):
    total_sum = 0

    for i in range(number):

        if i % 3 == 0 or i % 5 == 0:
            total_sum = total_sum + i

    return total_sum
