test_cases = int(input())
if test_cases>=1 and test_cases<=1000:
    def ans_giver(tesra):
        t = 0
        while t < tesra:
            b = 0
            n,k = input().split()
            value_of_n = int(n)
            value_of_k = int(k)
            if value_of_n>=1 and value_of_n<=100:
                if value_of_k>=1 and value_of_k<=10**5:
                    list_of_n_values = list(map(int, input().split()))
                    if len(list_of_n_values) == value_of_n:
                        # print(list_of_n_values)
                        for r in range(value_of_n):
                            if list_of_n_values[r]>10**5 or list_of_n_values[r]<1:
                                b = 1
                        if b == 0:
                            sum = 0
                            for i in range(value_of_n):
                                sum = sum + list_of_n_values[i]

                            if sum%value_of_k == 0:
                                print("0")
                                t = t + 1
                            else:
                                print("1")
                                t = t + 1
                        else:
                            t = t + 1
                    else:
                        t = t + 1
            else:
                t = t + 1
    ans_giver(test_cases)          
else:
    exit()