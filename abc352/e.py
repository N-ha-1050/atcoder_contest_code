from atcoder.dsu import DSU


def main():
    N, M = map(int, input().split())
    K, C, A = [], [], []
    for _ in range(M):
        k, c = map(int, input().split())
        a = [int(a_) - 1 for a_ in input().split()]
        K.append(k)
        C.append(c)
        A.append(a)
    res = solve(N, M, K, C, A)
    print(res)


def solve(N, M, K, C, A):

    # コストの昇順にソートする
    idxs = sorted(range(M), key=lambda x: C[x])

    # Union-Find を構築
    dsu = DSU(N)

    # クラスカル法
    res = 0
    for idx in idxs:
        for a in A[idx]:
            if not dsu.same(A[idx][0], a):
                dsu.merge(A[idx][0], a)
                res += C[idx]

    return res if dsu.size(0) == N else -1


if __name__ == "__main__":
    main()
