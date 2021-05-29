no_of_test_cases = int(input())
test = 0

a_value_in_given_pairs = []
b_value_in_given_pairs = []
while test < no_of_test_cases:
    the_value_a, the_value_b = input().split()
    a_value_in_given_pairs.append(the_value_a)
    b_value_in_given_pairs.append(the_value_b)
    test = test + 1

def even_number_count_giver(number1):
    if number1%2==0:
        even_numbers = number1/2
    else:
        even_numbers = (number1-1)/2
    return int(even_numbers)

def odd_number_count_giver(number2):
    if number2%2==0:
        odd_numbers = number2/2
    else:
        odd_numbers = ((number2-1)/2) + 1
    return int(odd_numbers)

for i in range(no_of_test_cases):
    if no_of_test_cases >= 1 and no_of_test_cases <= 1000:
        if int(a_value_in_given_pairs[i]) >= 1 and int(b_value_in_given_pairs[i]) <= 10**9 and int(a_value_in_given_pairs[i]) <= 10**9 and int(b_value_in_given_pairs[i]) >= 1:
            print((even_number_count_giver(int(a_value_in_given_pairs[i]))*even_number_count_giver(int(b_value_in_given_pairs[i])))+(
                odd_number_count_giver(int(a_value_in_given_pairs[i]))*odd_number_count_giver(int(b_value_in_given_pairs[i]))))
        else:
            exit()
    else:
        exit()
