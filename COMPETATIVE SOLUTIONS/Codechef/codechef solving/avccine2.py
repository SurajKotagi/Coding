user_input = input()
number_of_tests = int(user_input)
list_of_results = list()
def number_of_least_day_giver(ages_of_people_1, total_no_of_people_1, no_of_vaccines_per_day_1):
    
    error = 0
    no_of_days = 0
    no_of_people_at_risk = 0
    no_of_people_who_are_not_at_risk = 0
    for people in range(int(total_no_of_people_1)):
        if int(ages_of_people_1[people]) >= 1 and int(ages_of_people_1[people]) <= 100:
            if int(ages_of_people_1[people]) >= 80 or int(ages_of_people_1[people]) <= 9  :
                no_of_people_at_risk = no_of_people_at_risk + 1
        
            else:
                no_of_people_who_are_not_at_risk = no_of_people_who_are_not_at_risk + 1

        else:
            error = 1
    # print(no_of_people_at_risk)
    # print(no_of_people_who_are_not_at_risk)
    if no_of_people_at_risk%no_of_vaccines_per_day_1==0:
        no_of_days = no_of_people_at_risk/no_of_vaccines_per_day_1
    else:
        no_of_days = ((no_of_people_at_risk-(no_of_people_at_risk%no_of_vaccines_per_day_1))/no_of_vaccines_per_day_1) + 1

    if no_of_people_who_are_not_at_risk%no_of_vaccines_per_day_1==0:
        no_of_days = no_of_days + (no_of_people_who_are_not_at_risk/no_of_vaccines_per_day_1)
    else:
        no_of_days = no_of_days + ((no_of_people_who_are_not_at_risk-(no_of_people_who_are_not_at_risk%no_of_vaccines_per_day_1))/no_of_vaccines_per_day_1) + 1

    return no_of_days, error

if number_of_tests<= 10 and number_of_tests >= 1:
    for test in range(number_of_tests):

        a, b = input().split()
        no_of_vaccines_per_day = int(b)
        total_no_of_people = int(a)
        ages_of_people = list(map(int, input().split()))
        if total_no_of_people >=1 and total_no_of_people<=10**4 and no_of_vaccines_per_day>=1 and no_of_vaccines_per_day <= 10**5:
            no_of_days, error = number_of_least_day_giver(ages_of_people, total_no_of_people, no_of_vaccines_per_day)
            if error == 1:
                continue
            else:
                list_of_results.append(no_of_days)

        else:
            continue


    for answer in range(number_of_tests):
        print(int(list_of_results[answer]))
else:
    exit()