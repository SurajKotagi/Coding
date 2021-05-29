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
            d=100001
            ans_1 = 0
            ans_2 = 0
            while a>=1 and a<=(N/2) and a<b:
                while b>=1 and b>a and b<=(N/2):
                    if ((M%a)%b)==((M%b)%a):
                        ans_1 = ans_1 + 1
                    if ((M%c)%d)==((M%d)%c):
                        ans_2 = ans_2 + 1
                    b = b + 1
                    d = d + 1
                b = a + 2
                d = c + 2
                a = a + 1 
                c = c + 1
            ans = ans_1 + ans_2
            print(ans)
else:
    exit()