no_of_test_case = int(input())
if no_of_test_case>=1 and no_of_test_case<=100000:


    test = 0
    while test < no_of_test_case:
        test  = test + 1

        value_of_N, value_of_x, value_of_k = input().split()
        N = int(value_of_N)
        x = int(value_of_x)
        k = int(value_of_k)

        if x>=1 and x<=(N+1) and N>=k and N<=10*9:
        # print(X)
        # print(a)
        # print(b)
            if (x%k)==0:
                print("YES")
            else:
                if (N+1)%k==(x%k):
                    print("YES")
                else:
                    print("NO")
else:
    exit()