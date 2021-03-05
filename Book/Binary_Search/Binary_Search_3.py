n, m = map(int, input().split())
arr = list(map(int, input().split()))
result = 0
start = 0
end = max(arr)

while start <= end:
    total = 0
    mid = (start + end) // 2

    for i in arr:
        if i > mid:
            total = total + (i - mid)
    if total < m:
        end = mid - 1
    else:
        start = mid + 1
        result = mid

print(result)
