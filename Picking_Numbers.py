import time
from math import gcd
import collections
from functools import wraps

def measure_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        s_time = time.time()
        result = func(*args, **kwargs)
        f_time = time.time() - s_time
        print('{}:{}sec'.format(func.__name__, f_time))
        return result
    return wrapper


@measure_time
def solve(n, a):
    #Complete this function

    a = sorted(a)
    count = []
    count2 = []
    for x in range(0, len(a)):
        for y in range(x+1, len(a)+1):
            if abs(min(a[x:y])-max(a[x:y])) <=1:
                count.append(len(a[x:y]))
                count2.append(a[x:y])
    return max(count), count2

if __name__ == "__main__":
    n = 6
    s = [1,1,1,1,2,2,2,2,1]
    result = solve(n, s)
    print(result)