# 인덱스 바꾸기
# 틀렸습니다~

def solution(my_string, num1, num2):

    convert = list(my_string)
#print(list('hello'))
    
    convert[num1] = convert[num2]
    convert[num2] = convert[num1]

    return "".join(convert)


print(solution('hello', 1, 2))