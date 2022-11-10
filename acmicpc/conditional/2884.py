hour, min = map(int, input().split())

cal_hour = hour
cal_min = min - 45

if cal_min < 0:
    # 시간 계산
    if cal_hour - 1 < 0:
        cal_hour = 23
    else:
        cal_hour -= 1 

    # 분 계산
    cal_min += 60



print(cal_hour, cal_min)