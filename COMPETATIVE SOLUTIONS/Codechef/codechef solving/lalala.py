d1, v1, d2, v2, p = input().split()
m = int(d1)
n = int(d2)
v1 = int(v1)
v2 = int(v2)
p = int(p)
d1 = m
d2 = n
if d2 >= 1 and d1 >= 1 and v1 >= 1 and v2 <= 100 and p >= 1 and p <= 1000:

    if d1 == d2:
        minimum_days = (p/(v1+v2))+m-1
        if minimum_days>int(minimum_days) and minimum_days<int(minimum_days+1):
            print(int(minimum_days+1))
        else:
            print(minimum_days)
        exit()

    production_1 = v1
    the_number_of_days_by_company_one = 1
    production = v2
    if d1 < d2:
        while d1 < d2:
            if production_1 >= p:
                print(the_number_of_days_by_company_one)
                exit()
            else:
                production_1 = production_1 + v1
                the_number_of_days_by_company_one = the_number_of_days_by_company_one + 1
            d1 = d1 + 1
        # print(the_number_of_days_by_company_one)
        # print("lalalal")

    if d2 < d1:
        while d2 < d1:
            if production >= p:
                print(the_number_of_days_by_company_one)
                exit()
            else:
                production = production + v2
                the_number_of_days_by_company_one = the_number_of_days_by_company_one + 1
            d2 = d2 + 1
        # print(the_number_of_days_by_company_one)
        # print("laiksdnjksa")
    if m < n:
        production_both = (v2+v1+(the_number_of_days_by_company_one-1)*v1)
    if n < m:
        production_both = (v2+v1+(the_number_of_days_by_company_one-1)*v2)
    the_number_of_days_by_both_companies = the_number_of_days_by_company_one
    while production_both < p:
        production_both = production_both+v1+v2
        the_number_of_days_by_both_companies = the_number_of_days_by_both_companies+1
    # print(the_number_of_days_by_both_companies)
    # print("fscfadfd")

    if m > n:
        print(the_number_of_days_by_both_companies+n-1)

    if m < n:
        print(the_number_of_days_by_both_companies+m-1)

else:
    exit()