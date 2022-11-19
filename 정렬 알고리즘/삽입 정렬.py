# 처리되지 않은 데이터를 하나씩 골라 적절한 위치에 삽입
# 선택 정렬에 비해 구현 난이도가 높은 편이지만, 일반적으로 더 효율적으로 동작

array = [8, 3, 1, 0, 5, 9, 6, 2, 4, 7]

for i in range(len(array)):
    for j in range(i, 0, -1):
        if array[j] < array[j-1]:
            array[j-1], array[j] = array[j], array[j-1]
        else:
            break
print(array)

# 삽입 정렬은 선택 정렬과 같이 시간복잡도는 O(N^2)으로 이중반복문이 사용됨
# 선택 정렬과의 차이점은 현재 리스트가 데이터가 거의 정렬된 상태라면 매우 빠르게 동작
# 최선의 경우엔 O(N) 시간 복잡도