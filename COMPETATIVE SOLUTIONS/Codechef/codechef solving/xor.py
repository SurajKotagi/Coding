no_of_test_case = int(input())
if no_of_test_case>=1 and no_of_test_case<=(100000):


    test = 0
    while test < no_of_test_case:
        test  = test + 1

        N = int(input())
        mod = 1000000007
        
        if N>=1 and N<=100000:
            x=1
            ans = 1
            no_of_values = 0
            ans = 2**(N-1)
            print(ans%mod)

    
 
else:
    exit()
