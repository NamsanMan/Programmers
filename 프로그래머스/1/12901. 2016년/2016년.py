def solution(a, b):
    months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]

    passed_days = 0

    for i in range(a - 1):
        passed_days += months[i]

    passed_days += b - 1

    return days[passed_days % 7]