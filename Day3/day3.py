import os

daynumber = "3"
dataname = f"day{daynumber}.txt"

curdir = os.path.dirname(os.path.abspath(__file__))
filename = f'{curdir}\\{dataname}'
data = [_.strip() for _ in open(filename, 'r').readlines()]


def getPriorityValue1():
    totalSum = 0
    for str in data:
        str1 = set(str[0:len(str)//2])
        str2 = set(str[len(str)//2:])
        inter = str1 & str2
        for c in inter:
            print("Char c is " + c)

            temp = ord(c) - ord('a')
            if(temp < 0):
                
                temp = ord(c) - ord('A') + 27
                print("Temp1 val is ", temp)
            else:
                temp = temp + 1
                print("Temp2 val is ", temp)
            totalSum += temp
    print(totalSum)

def getPriority2():
    totalSum = 0
    for ind in range(0, len(data), 3):
        set1 = set(data[ind])
        set2 = set(data[ind + 1])
        set3 = set(data[ind + 2])
        inter = set1 & set2 & set3
        for c in inter:
            print("Char c is " + c)

            temp = ord(c) - ord('a')
            if(temp < 0):
                
                temp = ord(c) - ord('A') + 27
                print("Temp1 val is ", temp)
            else:
                temp = temp + 1
                print("Temp2 val is ", temp)
            totalSum += temp
    print(totalSum)
getPriority2()