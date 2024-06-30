def main():
    N, M, K = map(int, input().split())
    C = []
    A = []
    R = []
    for _ in range(M):
        c, *a, r = input().split()
        C.append(int(c))
        A.append(map(lambda x: int(x) - 1, a))
        R.append(True if r == "o" else False)
    res = solve(N, M, K, C, A, R)
    print(res)


def solve(N, M, K, C, A, R):

    # それぞれのテストの結果をbitに変換
    B = [0 for _ in range(M)]
    for i in range(M):
        for a in A[i]:
            B[i] ^= 1 << a

    res = 0

    # bit全探索で全ての鍵の組み合わせを調べる
    for i in range(1 << N):
        for b, r in zip(B, R):
            k = (i & b).bit_count()
            if r and k < K:
                break
            elif not r and k >= K:
                break
        else:
            res += 1

    return res


if __name__ == "__main__":
    main()
