test = 0 
test_cases = int(input())
if test_cases>=1 and test_cases<=10**3:
    while test < test_cases:

        n , k , d = input().split()

        value_of_n = int(n)
        if value_of_n>=1 and value_of_n<=10**2:

            value_of_k = int(k)
            if value_of_k<1 or value_of_k>10**9:
                test = test + 1
                continue 

            value_of_d = int(d)
            if value_of_k<1 or value_of_k>10**9:
                test = test + 1
                continue 

            total_number_of_problems = 0


            list_of_values = list(map(int, input().split()))
            if len(list_of_values)==value_of_n:
                for i in range(len(list_of_values)):
                    if list_of_values[i]<1 or list_of_values[i] > 10**7:
                        test = test + 1
                    total_number_of_problems = total_number_of_problems + list_of_values[i]
                if total_number_of_problems<value_of_k!=0:
                    print("0")
                    test = test + 1
                else:
                    a = (total_number_of_problems-(total_number_of_problems%value_of_k))/value_of_k
                    if a > value_of_d:
                        print(value_of_d)
                        test = test + 1

                    else:
                        print(int(a))
                        test = test + 1

            else:
                test = test + 1
        else:
            test = test + 1
           
else:
    exit()