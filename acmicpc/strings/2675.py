if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        add_string = ''
        repeat, string = input().split()
        for x in string:
            add_string += x * int(repeat)
        print(add_string)


