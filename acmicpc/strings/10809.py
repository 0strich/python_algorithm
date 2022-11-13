if __name__ == '__main__':
    X = input()
    alphabet = {}
    a, z = ord('a'), ord('z')

    for i in range(a, z+1):
        try:
            find_index = X.index(chr(i))
            alphabet[chr(i)] = find_index
        except:
            alphabet[chr(i)] = -1

    dictToList = list(map(str, alphabet.values()))
    print(' '.join(dictToList))

