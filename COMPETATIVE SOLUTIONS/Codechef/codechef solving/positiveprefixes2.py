value_of_k, value_of_n = input().split()
K = int(value_of_k)
N = int(value_of_n)
negetive_no_upto_n = list()
positive_no_upto_n = list()
modifier_list = list()
n = -1
m = 1 
for neg_value in range(N):
    positive_no_upto_n.append(m)
    negetive_no_upto_n.append(n)
    n = n - 1
    m = m + 1 

def sum_of_list_elements(upto,list):
    sum = 0
    count = 0
    while count < upto:
        sum = sum + int(list[count]) 
        count = count + 1
    return sum

# print(sum_of_list_elements(4, [2,3,4,6,7,8,9,5,6]))


x = 0
y = 0
lol = 0
while x+1 <= N:
    positives = 0
    z = -1
    y = 0
    modifier_list = list()
    for neg_value in range(N):
        modifier_list.append(z)
        z = z - 1
    print(modifier_list)
    # if sum_of_list_elements((x+1), modifier_list) < 0:
    modifier_list[x] = modifier_list[x]-(2*modifier_list[x])
    positives = positives + 1

    while (y+1) < N and lol==0:
        # if sum_of_list_elements((y+2), modifier_list) < 0:
        modifier_list[y+1] = modifier_list[y+1]-(2*modifier_list[y+1])
        positives = positives + 1
        if positives == value_of_k:
            print(modifier_list)
            lol = 1
        y = y + 1
    x = x + 1
