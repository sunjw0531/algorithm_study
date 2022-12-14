# 특정한 조건이 부합할 때만 사용할 수 있지만 매우 빠르게 동작하는 정렬 알고리즘
# 계수 정렬은 데이터의 크기 범위가 제한되어 정수 형태로 표현할 수 있을 때 사용 가능
# 데이터의 개수가 N, 데이터(양수) 중 최댓값이 K일 때, 최악의 경우에도 수행시간 O(N+K)를 보장
array = [8, 3, 1, 0, 5, 9, 6, 2, 4, 7, 1, 3, 5, 7, 3, 2, 5]
# 모든 범위를 포함하는 리스트 선언 (0으로 전부 초기화)
count = [0] * (max(array) +1)

for i in range(len(array)):
    count[array[i]] += 1    # 각 데이터에 해당하는 인덱스의 값 증가

for i in range(len(count)):  # 리스트에 기록된 정렬 정보 확인
    for j in range(count[i]):
        print(i, end=' ')   # 띄어쓰기를 구분으로 등장한 횟수만큼 인덱스 출력


# 계수 정렬의 시간 복잡도와 공간 복잡도는 모두 O(N+K)
# 계수 정렬은 때에 따라서 심각한 비효율성을 초래할 수 있음
# 계수 정렬은 동일한 값을 가지는 데이터가 여러 개 등장할 때 효과적으로 사용할 수 있음
