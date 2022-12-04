import os

daynumber = "4"
dataname = f"day{daynumber}.txt"

curdir = os.path.dirname(os.path.abspath(__file__))
filename = f'{curdir}\\{dataname}'
data = [_.strip() for _ in open(filename, 'r').readlines()]


def getResult1(r1, r2):
    #a-b, c-d

    ind1 = r1.index('-')
    ind2 = r2.index('-')
    a = (int)(r1[:ind1])
    b = (int)(r1[ind1+1:])
    c = (int)(r2[:ind2])
    d = (int)(r2[ind2+1:])
    if( (( c >= a and d <= b ) or ( a >= c and b <= d))  or ((a >= c and a <= d) or (b >= c and b <= d) ) ):
        return 1
    return 0

count1 = 0
count2 = 0
for val in data:
    pair = val.split(',')
    range1 = pair[0]
    range2 = pair[1]
    # print(range1, range2)
    # print(f'\n{getResult1(range1, range2)}')
    count1 += getResult1(range1, range2)
print(count1)
