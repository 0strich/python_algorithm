n = input().upper()
word = list(set(n))
word_count = []
 
 
for i in word:
    word_count.append(n.count(i))
 
temp = max(word_count)
if word_count.count(temp) > 1:
    print("?")
else:
    max_index = word_count.index(temp)
    print(word[max_index])