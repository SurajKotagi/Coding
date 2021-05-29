test_cases = int(input())
for test in range(test_cases):
    user_input1, user_input2 = input().split()
    value_of_K = int(user_input1)
    value_of_N = int(user_input2)
    if test_cases >= 1 and test_cases <= 1000 and value_of_K >= 1 and value_of_K <= 1000 and value_of_N >= 1 and value_of_N <= 1000 and value_of_K <= value_of_N:
        list_of_N = list()
        for i in range(1, value_of_N + 1):
            if i%2!=0:
                list_of_N.append(-i)
            else:
                list_of_N.append(i)
        # print(list_of_N)
        if value_of_K == value_of_N:
            value = 1
            while value <= value_of_N:
                print(value,end=" ")
                value = value + 1
            continue

        if value_of_N%2 == 0:
            positive_prefixes = value_of_N/2
        else:
            positive_prefixes = (value_of_N-1)/2

        i = 1
        while positive_prefixes < value_of_K:
            if list_of_N[value_of_N-i]>0:
                i = i + 1
            if list_of_N[value_of_N-1]<0:
                list_of_N[value_of_N-1] = list_of_N[value_of_N-1] - (2*list_of_N[value_of_N-1])
                positive_prefixes = positive_prefixes + 1
                i = i + 1


        while positive_prefixes > value_of_K:
            if list_of_N[value_of_N-i]>0:
                list_of_N[value_of_N-1] = list_of_N[value_of_N-1] - (2*list_of_N[value_of_N-1])
                positive_prefixes = positive_prefixes + 1
                i = i + 1
            if list_of_N[value_of_N-1]<0:
                i = i + 1

        for x in list_of_N:
            print(x, end=" ")
    else:
        continue