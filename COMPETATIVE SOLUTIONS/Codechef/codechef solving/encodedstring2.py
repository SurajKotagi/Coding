test = 0
test_cases = int(input())
if test_cases<1 or test_cases>10:
    exit()
while test < test_cases:
    value_of_n = int(input())
    a = str(input())

    if len(a)<4 or len(a)>10**5:
        test = test + 1
        continue
    if value_of_n%4==0:
        if len(a)==value_of_n:
            i = 0
            while i < len(a):
                if a[i] == '0':
                    if a[i+1] == '0':
                        if a[i+2] == '0':
                            if a[i+3] == '0':
                                if (i+4)==len(a):
                                    if (test+1)==test_cases:
                                        print("a",end="")
                                    else:
                                        print("a",end="\n")
                                else:
                                    print("a",end="")
                            else:
                                if (i+4)==len(a):
                                    if (test+1)==test_cases:
                                        print("b",end="")
                                    else:
                                        print("b",end="\n")
                                else:
                                    print("b",end="")
                        else:
                            if a[i+3] == '0':
                                if (i+4)==len(a):
                                    if (test+1)==test_cases:
                                        print("c",end="")
                                    else:
                                        print("c",end="\n")
                                else:
                                    print("c",end="")
                            else:
                                if (i+4)==len(a):
                                    if (test+1)==test_cases:
                                        print("d",end="")
                                    else:
                                        print("d",end="\n")
                                else:
                                    print("d",end="")
                    else:
                        if a[i+2] == '0':
                            if a[i+3] == '0':
                                if (i+4)==len(a):
                                    if (test+1)==test_cases:
                                        print("e",end="")
                                    else:
                                        print("e",end="\n")
                                else:
                                    print("e",end="")
                            else:
                                if (i+4)==len(a):
                                    if (test+1)==test_cases:
                                        print("f",end="")
                                    else:
                                        print("f",end="\n")
                                else:
                                    print("f",end="")
                        else:
                            if a[i+3] == '0':
                                if (i+4)==len(a):
                                    if (test+1)==test_cases:
                                        print("g",end="")
                                    else:
                                        print("g",end="\n")
                                else:
                                    print("g",end="")
                            else:
                                if (i+4)==len(a):
                                    if (test+1)==test_cases:
                                        print("h",end="")
                                    else:
                                        print("h",end="\n")
                                else:
                                    print("h",end="")

                else:
                    if a[i+1] == '0':
                        if a[i+2] == '0':
                            if a[i+3] == '0':
                                if (i+4)==len(a):
                                    if (test+1)==test_cases:
                                        print("i",end="")
                                    else:
                                        print("i",end="\n")
                                else:
                                    print("i",end="")
                            else:
                                if (i+4)==len(a):
                                    if (test+1)==test_cases:
                                        print("j",end="")
                                    else:
                                        print("j",end="\n")
                                else:
                                    print("j",end="")
                        else:
                            if a[i+3] == '0':
                                if (i+4)==len(a):
                                    if (test+1)==test_cases:
                                        print("k",end="")
                                    else:
                                        print("k",end="\n")
                                else:
                                    print("k",end="")
                            else:
                                if (i+4)==len(a):
                                    if (test+1)==test_cases:
                                        print("l",end="")
                                    else:
                                        print("l",end="\n")
                                else:
                                    print("l",end="")
                    else:
                        if a[i+2] == '0':
                            if a[i+3] == '0':
                                if (i+4)==len(a):
                                    if (test+1)==test_cases:
                                        print("m",end="")
                                    else:
                                        print("m",end="\n")
                                else:
                                    print("m",end="")
                            else:
                                if (i+4)==len(a):
                                    if (test+1)==test_cases:
                                        print("n",end="")
                                    else:
                                        print("n",end="\n")
                                else:
                                    print("n",end="")
                        else:
                            if a[i+3] == '0':
                                if (i+4)==len(a):
                                    if (test+1)==test_cases:
                                        print("o",end="")
                                    else:
                                        print("o",end="\n")
                                else:
                                    print("o",end="")
                            else:
                                if (i+4)==len(a):
                                    if (test+1)==test_cases:
                                        print("p",end="")
                                    else:
                                        print("p",end="\n")
                                else:
                                    print("p",end="")
                    # print(end="")
                
                i = i + 4
        else:
            test=test+1 
    else:
        test = test + 1
    test = test + 1
