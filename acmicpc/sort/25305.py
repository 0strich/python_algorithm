if __name__ == '__main__':
    a, b = map(int, input().split())
    scores = list(map(int, input().split()))
    scores.sort()
    scores.reverse()
    print(scores[b-1])


 
