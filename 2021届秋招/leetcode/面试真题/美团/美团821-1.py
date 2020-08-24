def main(string):
    record = [0, 0]
    n = len(string)
    for i in range(n):
        if i == 0 and not string[i].isalpha():
            print("Wrong")
            return
        if string[i].isdigit():
            record[0] += 1
        elif string[i].isalpha():
            record[1] += 1
        else:
            print("Wrong")
            return
    if record[0] == 0 or record[1] == 0:
        print("Wrong")
        return
    else:
        print("Accept")
        return

#
# T = int(input())
# k = 0
# while k < T:
#     string = input()
#     main(string)
#     k += 1
main("Ooook666")