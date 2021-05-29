no_of_tests = int(input())
if no_of_tests >= 1 and no_of_tests <= 100:
    def answer_giver():
        answer_list = []
        value_of_n = int(input())
        if value_of_n >= 1 and value_of_n <= 300:
            i = 0 
            while i < value_of_n:
                answer_list.append(0)
                i = i + 1
            # print(answer_list)

            input_list = list(map(int, input().split()))

            if len(input_list) == value_of_n:
                chance = 0
                for x in input_list:
                    if x < 1 or x > 10**9:
                        chance = 1
                if chance == 0:
                
                    pointer = 0
                    pointer_start = 0
                    pointer_end = value_of_n-1
                    while pointer < value_of_n:
                        if pointer%2==0:
                            answer_list[pointer] = input_list[pointer_start]
                            pointer =pointer + 1  
                            pointer_start = pointer_start + 1
                        else:
                            answer_list[pointer] = input_list[pointer_end]
                            pointer = pointer + 1
                            pointer_end = pointer_end - 1
                    print (*answer_list)
        
    test = 0
    while test < no_of_tests:
        answer_giver()
        test = test + 1
else:
    exit()
    """
6
7
3 4 5 2 9 1 1
4
9 2 7 1
11
8 4 3 1 2 7 8 7 9 4 2
1
42
2
11 7
8
1 1 1 1 1 1 1 1
"""
