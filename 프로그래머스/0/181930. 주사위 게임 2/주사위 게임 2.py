import math

def solution(a: int, b: int, c: int):
    answer = 0
    
    if a == b and a == c and b == c:
        answer = (a + b + c) * (math.pow(a, 2) + math.pow(b, 2) + math.pow(c, 2)) * (math.pow(a, 3) + math.pow(b, 3) + math.pow(c, 3))
    elif a == b or b == c or a == c:
        answer = (a + b + c) * (math.pow(a, 2) + math.pow(b, 2) + math.pow(c, 2))
    else:
        answer = a + b + c
        
    return answer