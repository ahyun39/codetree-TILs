string = list(str(input()))
set_string = set(string)
list_string = list(set_string)
if len(list_string) >= 2:
    print("Yes")
else:
    print("No")