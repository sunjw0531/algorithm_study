N = int(input())
array = []
for i in range(N):
    array.append(int(input()))
newArr = sorted(array, reverse=True)

for i in range(N):
    print(newArr[i], end=' ')