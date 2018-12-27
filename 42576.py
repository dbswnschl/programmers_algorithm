def solution(participant, completion):
    Map = {}
    for i in participant:
        if i not in Map:
            Map[i] = 1
        else:
            Map[i] = Map[i] +1
    for i in completion:
        Map[i] -= 1
    for i in Map:
        if Map[i] > 0 :
            return i


print(solution(	["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))
