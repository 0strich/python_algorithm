chess = list(map(int, input().split()))

right_piece = [1, 1, 2, 2, 2, 8]
result = ''

for i, v in enumerate(chess):
    result += str(right_piece[i] - v) + ' '

print(result[:-1])


