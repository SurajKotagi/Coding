test = 0
test_cases = int(input())
if 1<=test_cases and test_cases<=10*3:
    while test < test_cases:
        m , n = input().split()
        ameer_makandar_packs = int(m)
        if ameer_makandar_packs>=1:
            darshan_packs = int(n)
            if darshan_packs<=10*3:
                red_flag = 0 
                ameer_makandars_list = list(map(int, input().split()))
                if len(ameer_makandars_list)==ameer_makandar_packs:
                    for h in range(len(ameer_makandars_list)):
                        if ameer_makandars_list[h]>10*6 or ameer_makandars_list[h]<1:
                            red_flag = 1
                        if red_flag == 1:
                            break
                    if red_flag==1:
                        test = test + 1
                        continue
                else:
                    test = test + 1
                    continue
                darshans_list = list(map(int, input().split()))
                if len(darshans_list)==darshan_packs:
                
                    for q in range(len(darshans_list)):
                        if darshans_list[q]>10*6 or darshans_list[q]<1:
                            red_flag = 1
                        if red_flag == 1:
                            test = test + 1
                            continue
                    if red_flag==1:
                        test = test + 1
                        continue
                else:
                    test = test + 1
                    continue

                ameer_makandars_list.sort()
                darshans_list.sort()
                if ameer_makandar_packs >= 1 and darshan_packs <= 10*3:
                    ameer_makandars_total = 0   
                    for i in range(len(ameer_makandars_list)):
                        ameer_makandars_total = ameer_makandars_total + ameer_makandars_list[i]

                    darshans_total = 0   
                    for j in range(len(darshans_list)):
                        darshans_total = darshans_total + darshans_list[j]

                    if ameer_makandars_total > darshans_total:
                        print("0")
                    else:
                        step = 0
                        flag = 0
                        ameer_makandars_sum = 0
                        darshans_sum = 0    
                        pointer1 = 0
                        pointer2 = -1
                        if len(ameer_makandars_list)>=len(darshans_list):
                            for y in range(len(darshans_list)):
                                ameer_makandars_sum = 0
                                darshans_sum = 0 
                                temp = ameer_makandars_list[pointer1]
                                ameer_makandars_list[pointer1] = darshans_list[pointer2]
                                darshans_list[pointer2] = temp
                                pointer1 = pointer1 + 1
                                pointer2 = pointer2 - 1
                                step = step + 1
                                for l in range(len(ameer_makandars_list)):
                                    ameer_makandars_sum = ameer_makandars_sum + ameer_makandars_list[l]
                                for m in range(len(darshans_list)):
                                    darshans_sum = darshans_sum + darshans_list[m]
                                if ameer_makandars_sum<10*4 or darshans_sum<10*4: 
                                    if ameer_makandars_sum>darshans_sum:
                                        flag = 1
                                        break
                            if flag == 1:
                                if (test + 1)== test_cases: 
                                    print(step,end="")
                                else:
                                    print(step)                        
                            if flag == 0:
                                if (test + 1)== test_cases: 
                                    print("-1",end="")
                                else:
                                    print("-1")
                        if len(ameer_makandars_list) < len(darshans_list):
                            
                            for v in range(len(ameer_makandars_list)):
                                ameer_makandars_sum = 0
                                darshans_sum = 0
                                temp = darshans_list[pointer2]
                                darshans_list[pointer2] = ameer_makandars_list[pointer1]
                                ameer_makandars_list[pointer1] = temp
                                pointer1 = pointer1 + 1
                                pointer2 = pointer2 - 1
                                step = step + 1
                                for t in range(len(ameer_makandars_list)):
                                    ameer_makandars_sum = ameer_makandars_sum + ameer_makandars_list[t]
                                for r in range(len(darshans_list)):
                                    darshans_sum = darshans_sum + darshans_list[r]
                                if ameer_makandars_sum<10*4 or darshans_sum<10*4: 
                                    if ameer_makandars_sum>darshans_sum:
                                        flag = 1
                                        break
                                else:
                                    test = test + 1
                                    red_flag = 1
                            if flag == 1:
                                if (test + 1)== test_cases: 
                                    print(step,end="")
                                else:
                                    print(step)
                                
                            if flag == 0:
                                # print(ameer_makandars_list)
                                # print(darshans_list)
                                if (test + 1)== test_cases: 
                                    print("-1",end="")
                                else:
                                    print("-1")
                    
        test = test + 1
else:
    exit()