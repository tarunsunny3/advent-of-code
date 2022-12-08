import os

daynumber = "8"
dataname = f"day{daynumber}.txt"

curdir = os.path.dirname(os.path.abspath(__file__))
filename = f'{curdir}\\{dataname}'
data = [ [int(c) for c in _.strip()] for _ in open(filename, 'r').readlines()]
rows = len(data)
cols = len(data[0])
def checkDirUp(val, row, col, question):
    ans = 0
    for ind in range(row-1, -1, -1):
        if data[ind][col] >= val:
            ans += 1
            if(question == '1'):
                return False
            return ans
        ans += 1
    if(question == '1'):
        return True
    return ans

def checkDirDown(val, row, col, question):
    ans = 0
    for ind in range(row+1, rows):
        if data[ind][col] >= val:
            ans += 1
            if(question == '1'):
                return False
            return ans
        ans += 1
    if(question == '1'):
        return True
    return ans

def checkDirLeft(val, row, col, question):
    ans = 0
    for ind in range(col-1, -1, -1):
        if data[row][ind] >= val:
            ans += 1
            if(question == '1'):
                return False
            return ans
        ans += 1
    if(question == '1'):
        return True
    return ans

def checkDirRight(val, row, col, question):
    ans = 0
    for ind in range(col+1, cols):
        if data[row][ind] >= val:
            ans += 1
            if(question == '1'):
                return False
            return ans
        ans += 1
    if(question == '1'):
        return True
    return ans

def isValid(row, col):
    val = data[row][col]
   
    ans = checkDirUp(val, row, col, '1') or checkDirDown(val, row, col, '1') or checkDirLeft(val, row, col, '1') or checkDirRight(val, row, col, '1')
    return ans



def getScenicScore(row, col):
    val = data[row][col]
   
    ans = checkDirUp(val, row, col, '2') * checkDirDown(val, row, col, '2') * checkDirLeft(val, row, col, '2') * checkDirRight(val, row, col, '2')
    return ans

def scenicScore():
    maxScore = -1
    for r in range(1, rows-1):
        for c in range(1, cols-1):
            currScore = getScenicScore(r,c)
            maxScore = max(maxScore, currScore)
            # print(f"val is r={r}, c= {c}and val = {data[r][c]}, score = {currScore}")
    return maxScore

def answer1():
    ans = 2* rows + 2*(cols-2)
    for r in range(1, rows-1):
        for c in range(1, cols - 1):
            if(isValid(r,c)):
                # print(f"val is r={r}, c= {c}and val = {data[r][c]}")
                ans += 1
    return ans
print(f"Answer 1 is {answer1()}")
print(f"Answer 2 is {scenicScore()}")