# n = int(input())
#
# time = [n+1, 0, 0]
# count = 0
# for i in range(n*3600):
#     if '3' in str(time[0]) + str(time[1]) + str(time[2]):
#         count += 1
#     time[2] -= 1
#     if time[2] < 0:
#         time[1] -= 1
#         if time[1] < 0:
#             time[0] -= 1
#             time[1] = 59
#         time[2] = 59
#
# print(count)

n = int(input())
count = 0
for i in range(n+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)