array = [8, 3, 1, 0, 5, 9, 6, 2, 4, 7]

for i in range(len(array)):
    min_index = i
    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]

print(array)

# 선택 정렬은 N번 만큼 가장 작은 수를 찾아서 맨 앞으로 보내야 함
# 구현 방식에 따라서 사소한 오차는 있을 수 있지만, 전체 연산 횟수는 다음과 같음
# N + (N-1) + (N-2) + ... + 2
# 이는 (N^2 + N -2) /2 로 표현 가능한데, 빅오 표기법으로 O(N^2)이라고 작성