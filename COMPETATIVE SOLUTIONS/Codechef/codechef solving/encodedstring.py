test = 0 
test_cases = int(input())
if test_cases<1 or test_cases>10:
    exit()
else:
    while test < test_cases:
        # lines = 0
        # print("\n")
        value_of_n = int(input())
        list_of_binaries = list(map(str, input().split()))
        # print(len(list_of_binaries[0]))
        if len(list_of_binaries[0])<4 or len(list_of_binaries[0])>10**5:
            test = test + 1
            continue
        if value_of_n%4==0:
            if len(list_of_binaries[0])==value_of_n:
                i = 0
                a = list_of_binaries[0]
                # print(list_of_binaries[0])
                # print(a[1])
                while i < value_of_n:
                    if a[i]=='0':
                        if a[i+1]=='0':
                            if a[i+2]=='0':
                                if a[i+3]=='0':
                                    print("a",end="")
                                else:
                                    print("b",end="")
                            else:
                                if a[i+3]=='0':
                                    print("c",end="")
                                else:
                                    print("d",end="")
                        else:
                            if a[i+2]=='0':
                                if a[i+3]=='0':
                                    print("e",end="")
                                else:
                                    print("f",end="")
                            else:
                                if a[i+3]=='0':
                                    print("g",end="")
                                else:
                                    print("h",end="")
                        i = i + 4

                    else:
                        if a[i+1]=='0':
                            if a[i+2]=='0':
                                if a[i+3]=='0':
                                    print("i",end="")
                                else:
                                    print("j",end="")
                            else:
                                if a[i+3]=='0':
                                    print("k",end="")
                                else:
                                    print("l",end="")
                        else:
                            if a[i+2]=='0':
                                if a[i+3]=='0':
                                    print("m",end="")
                                else:
                                    print("n",end="")
                            else:
                                if a[i+3]=='0':
                                    print("o",end="")
                                else:
                                    print("p",end="")
                        i = i + 4
                print("\n")
                test = test + 1
            else:
                test=test+1 
        else:
            test = test + 1
    # print("\n")
