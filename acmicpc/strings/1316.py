result = 0
for i in range(int(input())):
    word = input()
    if list(word) == sorted(word, key=word.find):   # str sort
        result += 1
print(result)