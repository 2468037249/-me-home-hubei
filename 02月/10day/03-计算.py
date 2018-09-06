from functools import reduce
year = int(input('year:\n'))
month = int(input('month:\n'))
days = int(input('days:\n'))

months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]
leap_moths = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30]


def de_leap(year):
    if (year % 400 == 0) or (year % 4 == 0) and (year % 100 != 0):
        return True
    else:
        return False


if de_leap(year):
    sum = reduce(lambda x, y: x + y, leap_moths[:month]) + int(days)
    print("这是第%d天" % sum)

else:
    sum = reduce(lambda x, y: x + y, months[:month]) + int(days)
    print("这是第%d天" % sum)

