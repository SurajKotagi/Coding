no_of_test_case = int(input())
if no_of_test_case>=1 and no_of_test_case<=(3**9):


    test = 0
    while test < no_of_test_case:
        test  = test + 1

        word_one = str(input())
        word_two = str(input())
        word_three = str(input())
        row_one = list(word_one)
        row_two = list(word_two)
        row_three = list(word_three)
        # row_one = [item for item in input().split()]
        # row_two = [item for item in input().split()]
        # row_three = [item for item in input().split()]
        breaker = 0
        no_of_x = 0
        no_of_dash = 0
        no_of_y = 0
        slashes = 0
        salsh_of_o = 0
        salsh_of_x = 0
        wrong_input = 0
        for x in range(3):
            if row_one[x]=='X':
                no_of_x = no_of_x + 1
            if row_one[x]=='O':
                no_of_y = no_of_y + 1
            if row_one[x]=='_':
                no_of_dash = no_of_dash + 1
            if row_one[x]!='X' and row_one[x]!='O' and row_one[x]!='_':
                wrong_input = 1
            if row_two[x]=='X':
                no_of_x = no_of_x + 1
            if row_two[x]=='O':
                no_of_y = no_of_y + 1
            if row_two[x]=='_':
                no_of_dash = no_of_dash + 1
            if row_two[x]!='X' and row_two[x]!='O' and row_two[x]!='_':
                wrong_input = 1
            if row_three[x]=='X':
                no_of_x = no_of_x + 1
            if row_three[x]=='O':
                no_of_y = no_of_y + 1
            if row_three[x]=='_':
                no_of_dash = no_of_dash + 1    
            if row_three[x]!='X' and row_three[x]!='O' and row_three[x]!='_':
                wrong_input = 1  
            # print(f"wrong input {wrong_input}")
        if wrong_input==1:
            continue   
        if no_of_dash==9:
            print('2')
        else:
            if no_of_y-no_of_x==0 or no_of_x-no_of_y==1:
                
                for i in range(3):
                    if row_one[i]==row_two[i]==row_three[i] and row_one[i]!='_':
                        slashes= slashes + 1
                        if row_one[i]=='X':
                            salsh_of_x = salsh_of_x + 1
                        if row_one[i]=='O':
                            salsh_of_o = salsh_of_o + 1


                
                if row_one[0]==row_one[1]==row_one[2] and row_one[0]!='_':
                    slashes = slashes + 1
                    if row_one[0]=='X':
                        salsh_of_x = salsh_of_x + 1
                    if row_one[0]=='O':
                        salsh_of_o = salsh_of_o + 1
                if row_two[0]==row_two[1]==row_two[2] and row_two[0]!='_':
                    slashes = slashes + 1
                    if row_two[0]=='X':
                        salsh_of_x = salsh_of_x + 1
                    if row_two[0]=='O':
                        salsh_of_o = salsh_of_o + 1
                if row_three[0]==row_three[1]==row_three[2] and row_three[0]!='_':
                    slashes = slashes + 1
                    if row_three[0]=='X':
                        salsh_of_x = salsh_of_x + 1
                    if row_three[0]=='O':
                        salsh_of_o = salsh_of_o + 1
                if row_one[0]==row_two[1]==row_three[2] and row_three[2]!='_':
                    slashes = slashes + 1
                    if row_one[0]=='X':
                        salsh_of_x = salsh_of_x + 1
                        # print('diagonal slash by x')
                    if row_one[0]=='O':
                        salsh_of_o = salsh_of_o + 1
                        # print('diagonal slash by o')
                    # print('')
                if row_three[0]==row_two[1]==row_one[2] and row_three[0]!='_':
                    slashes = slashes + 1
                    if row_three[0]=='X':
                        salsh_of_x = salsh_of_x + 1
                    if row_three[0]=='O':
                        salsh_of_o = salsh_of_o + 1
                
                if no_of_x==4 and no_of_y==4:
                    # if slashes==0:
                        for x in range(3):
                            if row_one[x]=='_':
                                row_one[x] = 'X'
                            if row_one[x]=='_':
                                row_one[x] = 'X'
                            if row_two[x]=='_':
                                row_two[x] = 'X'
                            if row_two[x]=='_':
                                row_two[x] = 'X'
                            if row_three[x]=='_':
                                row_three[x] = 'X'
                            if row_three[x]=='_':
                                row_three[x] = 'X'  
                        for i in range(3):
                            if row_one[i]==row_two[i]==row_three[i] and row_one[i]!='_':
                                slashes= slashes + 1
                                if row_one[i]=='X':
                                    salsh_of_x = salsh_of_x + 1
                                if row_one[i]=='O':
                                    salsh_of_o = salsh_of_o + 1


                
                        if row_one[0]==row_one[1]==row_one[2] and row_one[0]!='_':
                            slashes = slashes + 1
                            if row_one[0]=='X':
                                salsh_of_x = salsh_of_x + 1
                            if row_one[0]=='O':
                                salsh_of_o = salsh_of_o + 1
                        if row_two[0]==row_two[1]==row_two[2] and row_two[0]!='_':
                            slashes = slashes + 1
                            if row_two[0]=='X':
                                salsh_of_x = salsh_of_x + 1
                            if row_two[0]=='O':
                                salsh_of_o = salsh_of_o + 1
                        if row_three[0]==row_three[1]==row_three[2] and row_three[0]!='_':
                            slashes = slashes + 1
                            if row_three[0]=='X':
                                salsh_of_x = salsh_of_x + 1
                            if row_three[0]=='O':
                                salsh_of_o = salsh_of_o + 1
                        if row_one[0]==row_two[1]==row_three[2] and row_three[2]!='_':
                            slashes = slashes + 1
                            if row_one[0]=='X':
                                salsh_of_x = salsh_of_x + 1
                                # print('diagonal slash by x')
                            if row_one[0]=='O':
                                salsh_of_o = salsh_of_o + 1
                                # print('diagonal slash by o')
                            # print('')
                        if row_three[0]==row_two[1]==row_one[2] and row_three[0]!='_':
                            slashes = slashes + 1
                            if row_three[0]=='X':
                                salsh_of_x = salsh_of_x + 1
                            if row_three[0]=='O':
                                salsh_of_o = salsh_of_o + 1
                        if salsh_of_x>=1:
                            print("2")
                            breaker=1
                if breaker == 1:
                    continue
                if no_of_x==5 and no_of_y==4:
                    if slashes==0:
                        print("1")
                    if slashes==1 or slashes==2:
                        print("1")
                else:
                    if slashes==1 and no_of_y!=no_of_x and salsh_of_o==1 and salsh_of_x==0:
                        print('3')
                        continue
                    if slashes==1 and no_of_y==no_of_x and salsh_of_x==0 and salsh_of_o==1:
                    # if slashes==1:
                        print("1")
                        continue
                    if slashes==1 and no_of_y==no_of_x and salsh_of_x==1 and salsh_of_o==0:
                    # if slashes==1:
                        print("3")
                        continue
                    if slashes==1 and no_of_x!=no_of_y and salsh_of_o==0 and salsh_of_x==1:
                        print("1")
                        continue
                    if slashes==1 and no_of_y==no_of_x and salsh_of_x==1 and salsh_of_o==0:
                    # if slashes==1:
                        print("3")
                        continue
                    if slashes>1:
                        print("3")
                        continue
                    if slashes!=1 and slashes<1:
                        print("2")
                        continue
            else:
                print("3")
else:
    exit()