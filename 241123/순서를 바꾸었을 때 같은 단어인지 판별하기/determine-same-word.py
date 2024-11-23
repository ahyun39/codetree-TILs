first_word = list(str(input()))
second_word = list(str(input()))

first_word.sort()
second_word.sort()

if first_word == second_word:
    print("Yes")
else:
    print("No")