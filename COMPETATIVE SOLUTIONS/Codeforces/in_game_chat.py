test_cases = int(input())
def answer_giver():
    string_length = int(input())
    no_of_p = 0
    given_string = str(input())
    if string_length == len(given_string):
        for i in range(len(given_string)):
            if given_string[len(given_string)-i-1] == ")":
                no_of_p = no_of_p + 1
            else:
                break

        if no_of_p > (len(given_string)-no_of_p):
            print("YES")
        else:
            print("NO")

for test in range(test_cases):
    answer_giver()