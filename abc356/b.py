def main():
    N, M = map(int, input().split())
    A = [int(a) for a in input().split()]
    X = [[int(x) for x in input().split()] for _ in range(N)]
    res = solve(N, M, A, X)
    print("Yes" if res else "No")


def solve(N, M, A, X):
    for i in range(M):

        # i番目の栄養素の合計摂取量を求める
        s = 0
        for j in range(N):
            s += X[j][i]

        # i番目の栄養素の合計摂取量が目標に達していなければその時点でNo
        if s < A[i]:
            return False
    return True


if __name__ == "__main__":
    main()
