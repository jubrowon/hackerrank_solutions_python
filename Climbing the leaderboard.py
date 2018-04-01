import random

def climbingLeaderboard(s, a):
    #
    # Write your code here.
    #
    # this solution caused time complexity to few problems so hope you to get it faster.
    rank = []
    mid = 0
    a = (x for x in a)

    for i in a:
        s.append(i)
        s = sorted(list(set(s)), reverse=True)
        idex = s.index(i)
        if idex == 0:
            rank.append(1)
            s.remove(i)
        else:
            rank.append(idex + 1)
            s.remove(i)

    return rank

if __name__ == "__main__":
    scores = []
    alice = []
    for i in range(0, 2 * (10 * 9)):
        i = random.randrange(4 * 8, 100 * 9)
        scores.append(i)

    for j in range(0, 2 * (10 * 9)):
        j = random.randrange(4 ** 8, 100 ** 9)
        alice.append(j)

    result = climbingLeaderboard(scores, alice)
    print(result)