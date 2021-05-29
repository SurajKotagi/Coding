no_of_test_case = int(input())
if no_of_test_case>=1 and no_of_test_case<=1000:


    test = 0
    while test < no_of_test_case:
        test  = test + 1

        initial_temperature, value_of_a, value_of_b = input().split()
        X = int(initial_temperature)
        a = int(value_of_a)
        b = int(value_of_b)

        if X>=31 and X<=40 and a>=101 and a <=120 and b>=1 and b<=5:
        # print(X)
        # print(a)
        # print(b)
            maximum_solubility = int(a + ((100 - X)*b))
            print(maximum_solubility*10)
else:
    exit()