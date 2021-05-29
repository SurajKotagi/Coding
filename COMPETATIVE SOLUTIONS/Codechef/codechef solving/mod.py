no_of_test_case = int(input())
if no_of_test_case>=1 and no_of_test_case<=(1000):

    sum_of_n = 0
    test = 0
    while test < no_of_test_case:
        test  = test + 1

        A , B = input().split()
        N = int(A)
        M = int(B)
        sum_of_n = sum_of_n + N
        if sum_of_n > 1000000:
            exit()
        if N>=2 and N<=1000000 and M>=1 and M<=5000000:
            
            a=1
            b=2
            c=100000
            ans = 0
            while a>=1 and a<=N and a<b:
                while b>1 and b>a and b<=N:
                    if ((M%a)%b)==((M%b)%a):
                        ans = ans + 1
                    b = b + 1
                b = a + 2
                a = a + 1 
            print(ans)
else:
    exit()