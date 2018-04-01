import sys


def formingMagicSquare(s):
    # Complete this function

    pixed_case = [[4, 9, 2, 3, 5, 7, 8, 1, 6], [8, 3, 4, 1, 5, 9, 6, 7, 2], [6, 1, 8, 7, 5, 3, 2, 9, 4],
                  [2, 7, 6, 9, 5, 1, 4, 3, 8], [8, 1, 6, 3, 5, 7, 4, 9, 2],
                  [4, 3, 8, 9, 5, 1, 2, 7, 6], [2, 9, 4, 7, 5, 3, 6, 1, 8], [6, 7, 2, 1, 5, 9, 8, 3, 4]]

    # ex) s 492 357 816
    OddMat = []
    dif = []
    for i in s:
        for y in i:
            OddMat.append(y)

    for x in pixed_case:
        sum = 0
        for y in range(len(x)):
            sum += abs(OddMat[y] - x[y])
        dif.append(sum)
    min_val = min(dif)

    return min_val


if __name__ == "__main__":
    s = [[4, 9, 2], [3, 5, 7], [8, 1, 6]]
    result = formingMagicSquare(s)
    print(result)