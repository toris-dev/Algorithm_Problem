from sys import stdin, stdout
import time
# 떡의 개수 n과 떡의 길이m 입력
starttime = time.time()
n, m = map(int, stdin.readline().split())

# 각 떡의 개별 높이 정보를 입력받기
h = list(map(int, stdin.readline().split()))

start = 0
end = max(h)

result = 0

# 이진 탐색 (반복적)
while(start <= end):
    total = 0
    mid = (start+end)//2
    for x in h:
        # 짤랐을때 떡의 양 계산
        if x > mid:
            total += x-mid
    # 떡의 양이 부족한 경우 더많이 자르기(왼쪽 부분 탐색)
    if total <= m:
        end = mid - 1
    # 떡의 양이 충분한 경우 덜 자리그 (오른쪽 탐색)
    else:
        result = mid
        start = mid + 1

print(result)
print(time.time() - starttime)
