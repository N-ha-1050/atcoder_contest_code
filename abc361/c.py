def main():
    N, K = map(int, input().split())
    A = [int(a) for a in input().split()]
    res = solve(N, K, A)
    print(res)


def solve(N, K, A):
    res = None
    dis = N - K
    sorted_A = sorted(A)
    for i in range(K + 1):
        r = sorted_A[i + dis - 1] - sorted_A[i]
        if res is None or r < res:
            res = r
    return res


if __name__ == "__main__":
    main()
