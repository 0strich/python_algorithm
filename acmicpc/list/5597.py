if __name__ == '__main__':
    students= [i for i in range(1, 31)]
    nums = []

    for i in range(28):
        nums.append(int(input()))

    for i in nums:
        students.remove(i)
 
    print(students[0])
    print(students[1])