def main():
    N = int(input())
    A = [int(a) for a in input().split()]
    res = solve(N, A)
    print(res)


def solve(N, A):
    MOD = 10**8

    sorted_A = sorted(A)

    res = 0
    idx = N - 1

    for i, a in enumerate(sorted_A):
        # a の分を先に足しておく
        res += a * (N - 1)

        # idx を一番うしろから見ていって、 a と足したとき MOD を超える間は、 idx を前に進める
        while 0 <= idx and sorted_A[idx] >= MOD - a:
            idx -= 1

        # a と足したとき MOD を超えるものの個数を計算
        cnt = N - max(i, idx) - 1

        # 超えた分の MOD を引く
        res -= MOD * cnt

    return res


if __name__ == "__main__":
    main()
