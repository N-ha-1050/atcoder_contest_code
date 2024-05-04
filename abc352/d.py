from sortedcontainers import SortedList


def main():
    N, K = map(int, input().split())
    P = [int(p) - 1 for p in input().split()]
    res = solve(N, K, P)
    print(res)


def solve(N, K, P):

    # Q[i] := (P_j = i となる j) で定義
    Q = [None for _ in range(N)]
    for i, p in enumerate(P):
        Q[p] = i

    # SortedList を定義
    sl = SortedList(Q[:K])  # 先頭K個
    res = sl[-1] - sl[0]  # 最大値 - 最小値

    # 区間を1ずらす
    for i in range(N - K):
        sl.remove(Q[i])
        sl.add(Q[i + K])
        res = min(res, sl[-1] - sl[0])

    return res


if __name__ == "__main__":
    main()
