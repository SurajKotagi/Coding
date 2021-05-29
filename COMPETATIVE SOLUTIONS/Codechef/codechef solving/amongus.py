no_of_test_cases = int(input())
if no_of_test_cases >= 1 and no_of_test_cases <= 10**3:
    test = 0 
        
    while test < no_of_test_cases:
        length_of_number = int(input())
        if length_of_number < 1 or length_of_number > 10**3:
            test = test + 1
            continue
        else:
            number_list = []
            number_list = list(map(int, input().split()))
            # print(number_list)
            even_numbbers = 0
            odd_numbers = 0
            # def Remove(duplicate): 
            #     final_list = [] 
            #     for num in duplicate: 
            #         if num not in final_list: 
            #             final_list.append(num) 
            #     return final_list 

            modifiied_list = number_list
            # for m in modifiied_list:
            #     a = countX(lst, i)
            #     if a > b:


            #     b = a
                 
            # print(modifiied_list)
            c = 0
            for i in modifiied_list:
                if i < 0 or i > 10**9:
                    test = test + 1
                    c = 1
                    continue
                elif i%2==0:
                    even_numbbers = even_numbbers + 1
                else:
                    odd_numbers = odd_numbers + 1
            if c == 0:
                if odd_numbers == 0:
                    ans = even_numbbers   
                elif even_numbbers == 0:
                    ans = odd_numbers
                elif even_numbbers > odd_numbers:
                    ans = even_numbbers + (2*(odd_numbers-1))

                else:
                    ans = odd_numbers + (2*(even_numbbers-1))

                print(ans)
                test = test + 1
            else:
                continue
    else:
        exit()