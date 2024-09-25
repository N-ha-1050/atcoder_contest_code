import bisect


def main():
    N, Q = map(int, input().split())
    A = [int(a) for a in input().split()]
    BK = [tuple(map(int, input().split())) for _ in range(Q)]
    res = solve(N, Q, A, BK)
    print(*res, sep="\n")


def solve(N, Q, A, BK):

    sorted_A = sorted(A)

    res = []
    for b, k in BK:

        def f(x):
            # 区間[b - x, b + x]に入るAの個数を求める
            l = bisect.bisect_left(sorted_A, b - x)
            r = bisect.bisect_right(sorted_A, b + x)
            return r - l

        # 区間 (l, r]で二分探索
        l, r = -1, max(abs(sorted_A[0] - b), abs(sorted_A[-1] - b))
        while r - l > 1:
            m = (l + r) // 2
            if f(m) >= k:
                r = m
            else:
                l = m
        res.append(r)
    return res


if __name__ == "__main__":
    main()
