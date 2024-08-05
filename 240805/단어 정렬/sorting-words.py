string_list = [input() for _ in range(int(input()))]
string_list.sort()
print(*string_list, sep='\n')