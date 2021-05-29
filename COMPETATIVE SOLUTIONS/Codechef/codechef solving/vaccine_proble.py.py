d1, v1, d2, v2, p = input().split()
if d2>d1:
    starting_day_of_company_1 = int(d1)
    starting_day_of_company_2 = int(d2)
    production_per_day_of_company_1 = int(v1)
    production_per_day_of_company_2 = int(v2)
else:   
    starting_day_of_company_1 = int(d2) 
    starting_day_of_company_2 = int(d1)
    production_per_day_of_company_1 = int(v2)
    production_per_day_of_company_2 = int(v1)
the_required_number_of_products = int(p)
days = 1

if  starting_day_of_company_1 >= 1 and starting_day_of_company_2 >= 1 and production_per_day_of_company_1 >= 1 and production_per_day_of_company_2 <= 100 and the_required_number_of_products >= 1 and the_required_number_of_products <= 1000:
    if starting_day_of_company_1 != starting_day_of_company_2:
        while days < starting_day_of_company_1:
            days = days + 1
        
        products_produced = 0

        while days >= starting_day_of_company_1 and days < starting_day_of_company_2 and products_produced < the_required_number_of_products:
            products_produced = products_produced + production_per_day_of_company_1
            days = days + 1

        while days >= starting_day_of_company_2 and products_produced < the_required_number_of_products:
            products_produced = products_produced + production_per_day_of_company_1 + production_per_day_of_company_2
            days = days + 1
    else:
        while days < starting_day_of_company_1:
            days = days + 1
        products_produced = 0
        while days >= starting_day_of_company_1 and products_produced < the_required_number_of_products:
            products_produced = products_produced + production_per_day_of_company_1 + production_per_day_of_company_2
            days = days + 1
print(days-1)