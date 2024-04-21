from atcoder.dsu import DSU


def main():
    N, M = map(int, input().split())
    AB = [tuple(map(int, input().split())) for _ in range(M)]
    res = solve(N, M, AB)
    print(res)


def solve(N, M, AB):
    def nC2(n):
        return n * (n - 1) // 2

    # DSU を定義
    G = DSU(N)

    for a, b in AB:
        G.merge(a - 1, b - 1)

    res = 0

    for i in range(N):
        if i != G.leader(i):
            continue

        # i が連結グラフの代表元のときのみ辺の本数を求めて加算
        res += nC2(G.size(i))

    res -= M
    return res


if __name__ == "__main__":
    main()
