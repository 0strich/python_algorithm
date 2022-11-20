if __name__ == '__main__':
    nums = []
    for i in range(5):
        nums.append(int(input()))

    nums.sort()
    print(int(sum(nums) / len(nums)))
    print(nums[2])
