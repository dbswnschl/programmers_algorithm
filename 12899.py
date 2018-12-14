# 문제가 개편 되었습니다. 이로 인해 함수 구성이 변경되어, 과거의 코드는 동작하지 않을 수 있습니다.
# 새로운 함수 구성을 적용하려면 [코드 초기화] 버튼을 누르세요. 단, [코드 초기화] 버튼을 누르면 작성 중인 코드는 사라집니다.
keyword = [1,2,4]
arr = []

def check(n):
    if n <= 0:
        return
    moc = int(n/3)
    nam = n % 3
    if nam == 0:
        arr.append(keyword[2])
        moc -= 1
    elif nam == 1:
        arr.append(keyword[0])
    else:
        arr.append(keyword[1])
    check(moc)
def solution(n):
    check(n)
    ret = ''
    for i in range(len(arr)):
        ret+=str(arr.pop())
    return ret


# 아래는 테스트로 출력해 보기 위한 코드입니다.
solution(1)