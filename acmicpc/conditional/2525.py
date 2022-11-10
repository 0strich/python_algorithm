hour, min = map(int, input().split())
add_min = int(input())

cal_hour = hour
cal_min = min + add_min

while cal_min >= 60:
    if cal_min >= 60:
        # 시간 계산
        if cal_hour + 1 >= 24:
            cal_hour = 0
        else:
            cal_hour += 1

        # 분 계산
        cal_min -= 60


print(cal_hour, cal_min)