if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        o_num = 0
        total = 0
        OX = input()
        for s in OX:
            if s == 'O':
                o_num += 1
            elif s == 'X':
                o_num = 0
            total += o_num
        print(total)

