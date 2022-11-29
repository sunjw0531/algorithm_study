N = int(input())
array = []
for i in range(N):
    student = input().split()
    array.append((student[0], int(student[1])))
array = sorted(array, key=lambda score:score[1])

for student in array:
    print(student[0], end=' ')