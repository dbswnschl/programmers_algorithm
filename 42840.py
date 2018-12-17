arr_p1 = [1, 2, 3, 4, 5]
arr_p2 = [2, 1, 2, 3, 2, 4, 2, 5]
arr_p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]


def solution(answers):
    answer = []
    score = [0, 0, 0]
    # player1
    for i in range(len(answers)):
        if arr_p1[i % len(arr_p1)] == answers[i]:
            score[0] += 1
        if arr_p2[i % len(arr_p2)] == answers[i]:
            score[1] += 1
        if arr_p3[i % len(arr_p3)] == answers[i]:
            score[2] += 1
    for i in range(3):
        if score[i] == max(score):
            answer.append(i+1)
    return answer


print(solution([1, 3,2,4,2]))
