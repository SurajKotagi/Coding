# user_input = input()
# no_of_test_cases = int(user_input)


user_input1, user_input2 = input().split()
value_of_K = int(user_input1)
value_of_N = int(user_input2)
list_of_N = list()
list_of_negetive_numbers_upto_N = list()
b = -1

for j in range(1, value_of_N + 1): 
    list_of_negetive_numbers_upto_N.append(b)
    list_of_N.append(j) 
    b = b - 1

def sum_upto_i(number,list):
    ans = 0
    for value in range(number-1):
        ans = ans + list[value]
    return ans

if value_of_K == value_of_N:
    value = 1
    while value <= value_of_N:
        print(value,end=" ")
        value = value + 1

else:
   
    prediction = 0
    i = 0
    while i < value_of_N:
        k = 0
        editor_list = list_of_negetive_numbers_upto_N
        if list_of_N[i] > sum_upto_i(int(list_of_N[i]),editor_list) and k < value_of_K:
            editor_list[i] = list_of_N[i]
            k =  k + 1
        if k == value_of_K:
            for m in range(i+1,value_of_N):
                if sum_upto_i(m, editor_list)<0:
                    print(editor_list)
        i = i + 1

# print(sum_upto_i(4,[1,2,3,4,5,6,7,]))