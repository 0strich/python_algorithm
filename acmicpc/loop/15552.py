import sys

if __name__ == "__main__":
    case = int(sys.stdin.readline())

    for i in range(case):
        a, b = map(int, sys.stdin.readline().split())
        print(a + b)
    
 