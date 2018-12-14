def solution(budgets, M):
    maximum = M
    arr = budgets.copy()
    arr.sort()
    line = arr[-1]
    while True:
        total = 0
        for i in range(len(arr)):
            if arr[i] <= line:
                total+=arr[i]
            else:
                total += line
        if total <= maximum:
            return line
        else:
            line -=1
print(solution([120, 110, 140, 150], 485))