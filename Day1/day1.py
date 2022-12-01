import os

daynumber = "1"
dataname = f"day{daynumber}.txt"
curdir = os.path.dirname(os.path.abspath(__file__))
filename = f'{curdir}\\{dataname}'
data = [_.strip() for _ in open(filename, 'r').readlines()]
data.append('')
calories = 0
res = []
maxVal = -1
for num in data:
    if num == '':
        res.append(calories)
        calories = 0
        continue
    calories += int(num)

# Answer to Part 1 
print(max(res))

# Answer to Part 2
print(sum(sorted(res, reverse=True)[0:3]))


