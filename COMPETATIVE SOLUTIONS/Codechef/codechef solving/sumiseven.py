no_of_test_cases = int(input())
test = 0

a_value_in_given_pairs = []
b_value_in_given_pairs = []
while test < no_of_test_cases:
    the_value_a, the_value_b = input().split()
    a_value_in_given_pairs.append(the_value_a)
    b_value_in_given_pairs.append(the_value_b)
    test = test + 1


def even_in_column_1_giver(number_1):
    n = 1
    even_numbers_in_column_1 = 0
    while n <= number_1:
        if n % 2 == 0:
            even_numbers_in_column_1 = even_numbers_in_column_1+1
        n = n + 1
    return even_numbers_in_column_1


def even_in_column_2_giver(number_2):
    m = 1
    even_numbers_in_column_2 = 0
    while m <= number_2:
        if m % 2 == 0:
            even_numbers_in_column_2 = even_numbers_in_column_2+1
        m = m + 1
    return even_numbers_in_column_2


def odd_in_column_1_giver(number_3):
    o = 1
    odd_numbers_in_column_1 = 0
    while o <= number_3:
        if o % 2 != 0:
            odd_numbers_in_column_1 = odd_numbers_in_column_1+1
        o = o + 1
    return odd_numbers_in_column_1


def odd_in_column_2_giver(number_4):
    p = 1
    odd_numbers_in_column_2 = 0
    while p <= number_4:
        if p % 2 != 0:
            odd_numbers_in_column_2 = odd_numbers_in_column_2+1
        p = p + 1
    return odd_numbers_in_column_2


for i in range(no_of_test_cases):
    if no_of_test_cases >= 1 and no_of_test_cases <= 1000:
        if int(a_value_in_given_pairs[i]) >= 1 and int(b_value_in_given_pairs[i]) <= 10**9 and int(a_value_in_given_pairs[i]) <= 10**9 and int(b_value_in_given_pairs[i]) >= 1:
            print((even_in_column_1_giver(int(a_value_in_given_pairs[i]))*even_in_column_2_giver(int(b_value_in_given_pairs[i])))+(
                odd_in_column_1_giver(int(a_value_in_given_pairs[i]))*odd_in_column_2_giver(int(b_value_in_given_pairs[i]))))
        else:
            exit()
    else:
        exit()
