a , b = input().split() 
value_one = int(a)
value_two = int(b)

sum = value_one + value_two
dif = value_one - value_two
mul = value_one * value_two
div = (value_one/value_two)

print(format(sum,".1f"))
print(format(dif,".1f"))
print(format(mul,".1f"))
print(format(div,".1f"))