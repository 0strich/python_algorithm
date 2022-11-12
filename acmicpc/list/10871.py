def filter(lst, cmp):
    result = []
    for i in lst:
        if i < cmp:
            result.append(str(i)) 
    return result

if __name__ == '__main__':
    A, X = map(int, input().split())
    lst = list(map(int, input().split()))
    result = filter(lst, X)
    print(' '.join(result))
 