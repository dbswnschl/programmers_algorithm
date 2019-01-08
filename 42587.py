def solution(priorities, location):
    loc = location
    cnt = 0
    while loc > -1:
        isChange = False
        first = priorities[0]
        for num in priorities[1:]:
            if first < num:
                isChange = True
                break
        if isChange:
            priorities.append(priorities.pop(0))
            if loc == 0:
                loc = len(priorities) -1
            else:
                loc -=1
        else:
            priorities.pop(0)

            if loc == 0:
                return cnt+1
            else:
                loc -= 1
            cnt +=1

    answer = 0
    return answer


print(solution(	[1, 1, 9, 1, 1, 1], 0))
