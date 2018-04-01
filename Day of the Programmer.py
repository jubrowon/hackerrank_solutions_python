import sys

def solve(year):
    # Complete this function
    julia_common = [31, 29 ,31 ,30 ,31 ,30 ,31 ,30 ,31 ,30 ,31 ,30]
    gregori_common = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    julia_leap = [31, 30 ,31 ,30 ,31 ,30 ,31 ,30 ,31 ,30 ,31 ,30]
    gregori_leap = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    d = 0
    m = 0
    y = 0

    def cal(julia_leap):
        d, m, y = 0, 0, 0

        for i in range(1, len(julia_leap) - 1):
            if -julia_leap[i + 1] < int(sum(julia_leap[0:i]) - 256) <= 0:
                d = (-int(sum(julia_leap[0:i]) - 256))
                m = '0'+str(i+1)
                y = year
        return d, m, y

    if 1700 <= year <= 1917:
        if year % 4 == 0:
            d, m, y = cal(julia_leap)
        else:
            d, m, y=cal(julia_common)
    else:
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            d, m, y = cal(gregori_leap)
        else:
            d, m, y = cal(gregori_common)
    if year == 1918:
        gregori_common[1] = 15
        d, m, y = cal(gregori_common)

    return '{0}.{1}.{2}'.format(d, m, y)


year = int(input().strip())
result = solve(year)
print(result)