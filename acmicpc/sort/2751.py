import sys

if __name__ == '__main__':
    n = int(input())
    nums = []
    for i in range(n):
        nums.append(int(sys.stdin.readline()))

    nums.sort()

    for i in nums:
        print(i)


