def solution(my_string, num1, num2):
    
    my_string[num1], my_string[num2] = my_string[num2], my_string[num1]
    
    return answer 


print(solution("hello", 1, 2))
print(solution("I love you", 3, 6))