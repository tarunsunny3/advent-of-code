import os

daynumber = "6"
dataname = f"day{daynumber}.txt"

curdir = os.path.dirname(os.path.abspath(__file__))
filename = f'{curdir}\\{dataname}'
data = open(filename, 'r').read()


def getAnswer(numberOfUniqueChars):
    for i in range(0, len(data)):

        st = set()

        substr = data[i:i+numberOfUniqueChars]

        for ind in range(0, numberOfUniqueChars):
            st.add(substr[ind])
            if(len(st) == numberOfUniqueChars):
                return i+numberOfUniqueChars


print(f"Answer 1 is {getAnswer(4)}")
print(f"Answer 2 is {getAnswer(14)}")
   
            
