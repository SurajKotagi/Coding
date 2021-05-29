test_cases = int(input())
if test_cases>=1 and test_cases<=1000:
    def answer_giver():
        lenght = int(input())
        if lenght >=4 and lenght <=200:
            user_input = str(input())
            if len(user_input) == lenght:
                if user_input[0] == "2" and user_input[-1] == "0" and user_input[-2] == "2" and user_input[-3] == "0":
                    print("YES")
                    return 0
                elif user_input[0] == "2" and user_input[1] == "0" and user_input[-1] == "0" and user_input[-2] == "2":
                    print("YES")
                    return 0
                elif user_input[0] == "2" and user_input[1] == "0" and user_input[2] == "2" and user_input[-1] == "0":
                    print("YES")
                    return 0
                elif user_input[0] == "2" and user_input[1] == "0" and user_input[2] == "2" and user_input[3] == "0":
                    print("YES")
                    return 0
                elif user_input[-1] == "0" and user_input[-2] == "2" and user_input[-3] == "0" and user_input[-4] == "2":
                    print("YES")
                    return 0
                else:
                    print("NO")
                    return 0
            else:
                return 0
        else:
            return 0 
    for i in range(test_cases):
        answer_giver()