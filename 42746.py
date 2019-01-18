
# def m_sort(arr,pivot=0):
#     left = []
#     if len(arr) <= 1:
#         return arr
#     val = [arr.pop(pivot)]
#     right = []
#     for i in range(len(arr)):
#         if arr[i] < val[0]:
#             left.append(arr[i])
#         else:
#             right.append(arr[i])
#     return m_sort(left)+val+m_sort(right)



def new_find(arr):
    tmp = arr.copy()
    most_len = 4
    for i in range(len(arr)):
        if len(arr[i]) == 1:
            tmp[i] = tmp[i] * 4
        elif len(arr[i]) == 2:
            tmp[i] += tmp[i]
        elif len(arr[i]) == 3:
            tmp[i] += tmp[0]
    tmp_tmp = tmp.copy()
    tmp.sort(reverse=True)
    result = []
    for i in tmp:
        idx = tmp_tmp.index(i)
        result.append(arr[idx])
        tmp_tmp[idx] = -1
    return result


def solution(numbers):
    arr = {}
    for i in range(len(numbers)):
        if str(numbers[i])[0] not in arr:
            arr[str(numbers[i])[0]] = []
        arr[str(numbers[i])[0]].append(str(numbers[i]))
    keys = list(arr.keys())
    keys.sort(reverse=True)
    answer = []
    for key in keys:
        if len(arr[key]) > 1:
            answer.append(new_find(arr[key]))
        else:
            answer.append(arr[key])
    result =''
    for i in answer:
        for j in i:
            result += j
    while True:
        if len(result)>1 and result[0] == '0':
            result = result[1:]
        else:
            break
    return str(result)

print(solution([1000,100,101]))