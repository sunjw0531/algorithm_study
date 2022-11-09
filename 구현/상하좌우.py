# N = int(input())
# x = 1
# y = 1
# moves = input().split()
#
# dy = [-1, 1, 0, 0]
# dx = [0, 0, -1, 1]
#
# for move in moves:
#     if move == 'L':
#         x += dx[0]
#         y += dy[0]
#     elif move == 'R':
#         x += dx[1]
#         y += dy[1]
#     elif move == 'U':
#         x += dx[2]
#         y += dy[2]
#     elif move == 'D':
#         x += dx[3]
#         y += dy[3]
#     if x == 0:
#         x = 1
#     elif x == 6:
#         x = 5
#     if y == 0:
#         y = 1
#     elif y == 6:
#         y = 5
# print(x, y)

n = int(input())
x, y = 1, 1
plans = input().split()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(move)):
        if plan == move[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx == 0 or ny == 0 or nx > n or ny > n:
        continue
    else:
        x = nx
        y = ny
print(x, y)