def solution(n, words):
    m_set = set()
    before = None
    for i,word in enumerate(words):
        turn = i % n
        game = i // n
        if i == 0:
            m_set.add(word)
            before = word
        else:
            # 끝말잇기 공식
            if before[-1] is not word[0]:
                return [turn+1,game+1]

            elif word not in m_set:
                m_set.add(word)
                before = word
            else: # 중복단어검출
                return [turn+1,game+1]
        if i == len(words) -1 :
            return [0,0]



print(solution(		2, ["hello", "one", "even", "never", "now", "world", "draw"]))