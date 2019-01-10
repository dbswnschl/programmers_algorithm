def solution(skill, skill_trees):
    cnt = 0
    for tree in skill_trees:
        sun = list(skill)
        for i,custom_skill in enumerate(tree):
            if len(sun) > 0 and custom_skill == sun[0]:
                sun.pop(0)
            elif len(sun)> 0 and custom_skill in sun:
                # print(f"선행스킬 {sun[0]} 필요 {custom_skill}")
                break
            if i == len(tree)-1:
                # print("스킬 +1")
                cnt +=1






    return cnt

print(solution(	"CBD", ["BACDE", "CBADF", "AECB", "BDA"]))