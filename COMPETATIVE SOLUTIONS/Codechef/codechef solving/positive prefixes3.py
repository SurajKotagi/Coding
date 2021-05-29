positive_no_list = [1, 2, 3, 4]
K = 2
N = 4
negetive_no_list = [-1, -2, -3, -4]
x = 0
while x < N:
    y = 0
    negetive_no_list = [-1, -2, -3, -4]
    negetive_no_list[x] = positive_no_list[x]
    while y < K-1:
        negetive_no_list[y+1] = positive_no_list[y+1]
        y = y + 1 
        print(negetive_no_list)
    x = x + 1 