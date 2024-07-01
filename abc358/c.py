def main():
    N, M = map(int, input().split())
    S = [input() for _ in range(N)]
    res = solve(N, M, S)
    print(res)


def solve(N, M, S):

    # bitに直す
    T = [sum(1 << i for i, t in enumerate(s) if t == "o") for s in S]

    # 全ての味を変えたときのbitの値
    R = (1 << M) - 1

    res = None

    # bit全探索
    for i in range(1 << N):
        r = 0  # 購入済みの味をbitで記録
        c = 0  # 訪問地点の個数
        for j in range(N):
            if (i >> j) & 1:
                r |= T[j]
                c += 1

        # すべて買えたかの判定
        if r == R:
            if res is None or c < res:
                res = c
    return res


if __name__ == "__main__":
    main()
