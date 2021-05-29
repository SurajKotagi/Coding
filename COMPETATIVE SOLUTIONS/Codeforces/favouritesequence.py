def answer_giver():
    
    lenght = int(input())
    user_input = str(input())
    if lenght%2 == 0:
        answer_list = []
        for i in range(lenght):
            answer_list.append("0")
        m = 0 
        n = (lenght - 1)
        x = 0
        y = int(lenght/2)
        while x < (lenght/2):
            answer_list[m] = user_input[x]
            m = m + 2
            answer_list[n] = user_input[y]
            n = n-2
            x = x + 1
            y = y + 1 
    for c in range(len(answer_list)):
        print(answer_list[c],end="")

answer_giver()
