def solution(genres, plays):
    songs = {}
    answer = {}
    for idx,genre in enumerate(genres):
        if genre not in songs:
            songs[genre] = {}
        songs[genre][idx] = plays[idx]
    result = set()
    for genre in songs:
        cnt = 0
        max1 = None
        max2 = None
        for id,val in songs[genre].items():
            cnt += val
            if max1 is None:
                max1 = [id,val]
            elif max2 is None:
                if max1[1] > val :
                    max2 = [id,val]
                elif max1[1] == val:
                    if max1[0] < id:
                        max2 = [id,val]
                    else:
                        max2 = max1[:]
                        max1 = [id,val]
                else:
                    max2 = max1[:]
                    max1 = [id,val]
            else:
                if val > max1[1]:
                    max2 = max1[:]
                    max1 = [id,val]
                elif val == max1[1]:
                    if max1[0] < id:
                        max2 = [id,val]
                    else:
                        max2 = max1[:]
                        max1 = [id,val]
                elif val > max2[1]:
                    max2 = [id,val]
                elif val == max2[1]:
                    if max2[0] > id:
                        max2 = [id,val]
        if max2 is not None:
            answer[genre] = [cnt,max1[0],max2[0]]
        else:
            answer[genre] = [cnt,max1[0]]
        result.add(cnt)
    final = []
    result = list(result)
    result.sort()
    for idx in range(len(result)-1,-1,-1):
        for j in answer.values():
            if j[0] == result[idx]:
                final.append(j[1])
                if len(j) > 2:
                    final.append(j[2])
                break
    return final
# print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
print(solution(['classic','pop','classic','pop','classic','classic'], [400,600,150,2500,500,500]))