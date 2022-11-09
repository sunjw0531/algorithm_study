pos = input()
x = int(ord(pos[0])-ord('a'))+1
y = int(pos[1])


steps = [(-2, -1), (-1, -2), (1,-2), (2, -1), (2,1), (1,2), (-1, 2), (-2, 1)]
count = 0
for step in steps:
    stepX = step[0] + x
    stepY = step[1] + y
    if stepX > 1 and stepY > 1 and stepX <8 and stepY <8:
        count+=1
print(count)
