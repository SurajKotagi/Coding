no_of_test_case = int(input())
if no_of_test_case>=1 and no_of_test_case<=3**9:


    test = 0
    while test < no_of_test_case:
        test  = test + 1

        row_one = str(input())
        row_two = str(input())
        row_three = str(input())

        column_one = ""
        column_two = ""
        column_three = ""

        
        column_one[0] = row_one[0]
        column_two[0] = row_one[1] 
        column_three[0] = row_one[2] 
        column_one[1] = row_two[0]
        column_two[1] = row_two[1] 
        column_three[1] = row_two[2] 
        column_one[2] = row_three[0]
        column_two[2] = row_three[1] 
        column_three[2] = row_three[2] 

        no_of_x = 0
        no_of_o = 0
        no_of_dash = 0

        slashes_by_x = 0
        slashes_by_o = 0

        for y in range(3):

            if row_one[y]=="X":
                no_of_x = no_of_x + 1
            if row_two[y]=="X":
                no_of_x = no_of_x + 1
            if row_three[y]=="X":
                no_of_x = no_of_x + 1

            if row_one[y]=="O":
                no_of_o = no_of_o + 1
            if row_two[y]=="O":
                no_of_o = no_of_o + 1
            if row_three[y]=="O":
                no_of_o = no_of_o + 1
            
            if row_one[y]=="_":
                no_of_dash = no_of_dash + 1
            if row_two[y]=="_":
                no_of_dash = no_of_dash + 1
            if row_three[y]=="_":
                no_of_dash = no_of_dash + 1

        if (no_of_x-no_of_o)==1 or (no_of_x-no_of_o)==0:

            for x in range(3):
                if row_one[x]==row_two[x]==row_three[x]!="_":
                    if row_one[x]=="X":
                        slashes_by_x = slashes_by_x + 1
                    if row_one[x]=="Y":
                        slashes_by_y = slashes_by_y + 1
                if column_one[x]==column_two[x]==column_three[x]!="_":
                    if column_one[x]=="X":
                        slashes_by_x = slashes_by_x + 1
                    if column_one[x]=="Y":
                        slashes_by_y = slashes_by_y + 1
                
            if row_one[0]==row_two[1]==row_three[2]!="_":
                if column_one[0]=="X":
                        slashes_by_x = slashes_by_x + 1
                if column_one[0]=="Y":
                    slashes_by_y = slashes_by_y + 1
            if row_one[2]==row_two[1]==row_three[0]!="_":
                if column_one[2]=="X":
                        slashes_by_x = slashes_by_x + 1
                if column_one[2]=="Y":
                    slashes_by_y = slashes_by_y + 1

            print(no_of_o)
            print(no_of_x)
            print(slashes_by_o)
            print(slashes_by_x)
        else:
            print("3")

















else:
    exit()