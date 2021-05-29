b = str(input())
def answer_giver(user_input):
    for i in range(int(user_input)):
        if int(str(user_input[i]))!=0:
            a = int(str(user_input[i]))
            if (int(user_input))%a!=0:
                answer_giver(int(user_input) + 1)
            else:
                print(user_input)


answer_giver(b)