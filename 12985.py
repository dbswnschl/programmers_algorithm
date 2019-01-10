def isOdd(num):
    if num % 2 == 1:
        return True
    else:
        return False
def display(a,b):
    if isOdd(a) and not isOdd(b):
        if a + 1 == b:
            # print("같은 경기")
            return True
    elif not isOdd(a) and isOdd(b):
        if b + 1 == a:
            # print("같은 경기")
            return True
    else:
        # print('다른 경기')
        return False
def solution(n,a,b):
    rnd = 1
    while not display(a,b):
        print(f'{rnd}라운드')
        print(f'선수들 {n}명 참가')
        print(f'{a}번 선수가 {b}번 선수를 만난다')

        display(a, b)
        rnd +=1
        n = n // 2
        if a % 2 == 1:
            a = a // 2 + 1
        elif a % 2 == 0:
            a = a // 2
        if b % 2 == 1:
            b = b // 2 + 1
        elif b % 2 == 0:
            b = b // 2

    return rnd

print(solution(8, 4, 7))