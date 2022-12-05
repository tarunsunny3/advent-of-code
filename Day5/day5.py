import os

daynumber = "5"
dataname = f"day{daynumber}.txt"

curdir = os.path.dirname(os.path.abspath(__file__))
filename = f'{curdir}\\{dataname}'
newData = ''
mainData = [_ for _ in open(filename, 'r').read().split('\n\n')]

def getTotalStacks(line):
    numbers = line.strip().split(' ')
    return int(numbers[len(numbers)-1])

def initializeStacks():
    stacks = []
    for i in range(0, totalStacks):
        stacks.append([])
    return stacks

def populateStacks(stacks):
    for val in stackData:
        stno = 0
        for ind in range(1, len(val), 4):
            if(val[ind] == ' '): 
                stno += 1
                continue
            stacks[stno].append(val[ind])
            stno += 1
    
    for stack in stacks:
        stack.reverse()

def applyTheMoves1(stacks):
    data = movesData.split('\n')
    for move in data:
        move = move.replace('move ', '')
        move = move.replace('from ', '')
        move = move.replace('to ', '')

        values = move.strip().split(' ')
        
        noOfItems = int(values[0])
        fromStack = int(values[1])
        toStack = int(values[2])


        while(noOfItems > 0):
            stacks[toStack-1].append(stacks[fromStack-1].pop())
            noOfItems -= 1

def applyTheMoves2(stacks):
    data = movesData.split('\n')
    for move in data:
        move = move.replace('move ', '')
        move = move.replace('from ', '')
        move = move.replace('to ', '')

        values = move.strip().split(' ')
        
        noOfItems = int(values[0])
        fromStack = int(values[1])
        toStack = int(values[2])

        toPush = stacks[fromStack-1][-1 * noOfItems:]
        for _ in range(0, noOfItems):
            stacks[fromStack-1].pop()
        for item in toPush:
            stacks[toStack-1].append(item)

def printAnswer(stacks):
    ans = ''
    for st in stacks:
        if(len(st) != 0):
            ans += st[len(st)-1]
    return ans

def star1():
    stacks = initializeStacks()
    populateStacks(stacks)
    applyTheMoves1(stacks)
    print(f"Answer 1 is {printAnswer(stacks)}")
    
    

def star2():
    stacks = initializeStacks()
    populateStacks(stacks)
    applyTheMoves2(stacks)
    print(f"Answer 2 is {printAnswer(stacks)}")

stackData = mainData[0].split('\n')

totalStacks = getTotalStacks(stackData[len(stackData)-1])

# Removing the last item of StackData which is [1,2,3....] the number labels of stacks
stackData.pop()

movesData = mainData[1]




star1()
star2()
