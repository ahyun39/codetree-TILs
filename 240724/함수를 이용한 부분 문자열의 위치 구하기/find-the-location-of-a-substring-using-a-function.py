def solution(string):
    for i in range(len(input_string)-len(string)+1):
        if input_string[i:i+len(string)] == string:
            return i
    return -1

input_string = str(input())
print(solution(str(input())))