from atcoder.segtree import SegTree


def main():
    N, K = map(int, input().split())
    P = [int(p) - 1 for p in input().split()]
    res = solve(N, K, P)
    print(res)


def solve(N, K, P):

    # セグメント木を定義
    st_min = SegTree(min, N, N)
    st_max = SegTree(max, -1, N)

    # st[i] := (P_j = i となる j)
    for i, p in enumerate(P):
        st_min.set(p, i)
        st_max.set(p, i)

    # 全ての区間で差の最大値を求める
    res = N
    for i in range(N - K + 1):
        j = i + K
        res = min(res, st_max(i, j) - st_min(i, j))

    return res


if __name__ == "__main__":
    main()
