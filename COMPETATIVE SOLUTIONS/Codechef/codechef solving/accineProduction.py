d1, v1, d2, v2, p = input().split()
d1 = int(d1)
d2 = int(d2)
v1 = int(v1)
v2 = int(v2)
p = int(p)
if d2>=1 and d1>=1 and v1>=1 and v2<=100 and p>=1 and p<=1000:
    if d1 == d2:
        minimum_days = ((v1+v2)/p)
    if d2 >= d1:
        a = p-((d2-d1)*v1)
        c = (v1+v2)
        b = d2-d1
        minimum_days = (a/c)+b+d1-1
    if d1 >= d2:
        a = p-((d1-d2)*v2)
        c = (v1+v2)
        b = d1-d2
        minimum_days = (a/c)+b+d2-1
    if minimum_days.is_integer():
        print(int(minimum_days))
    else:
        minimum_days = int(minimum_days+1)
        print(minimum_days)