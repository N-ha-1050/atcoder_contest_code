def main():
    N, K = map(int, input().split())
    A = [int(a) for a in input().split()]
    res = solve(N, K, A)
    print(*res, sep="\n")


def solve(N: int, K: int, A: list[int]) -> list[int]:
    # CPython だと TLE(PyPy なら通る)

    M = max(A)
    cnt = [0 for _ in range(M + 1)]
    for a in A:
        cnt[a] += 1
    cnt_mul = [0 for _ in range(M + 1)]  # cnt_mul[i] := A に含まれる i の倍数の個数
    for i in range(1, M + 1):
        for j in range(i, M + 1, i):
            cnt_mul[i] += cnt[j]
    mem = [0 for _ in range(M + 1)]  # mem[i] := i に対する問題の答え
    for i in reversed(range(1, M + 1)):
        if cnt_mul[i] < K:
            continue
        for j in range(i, M + 1, i):
            if mem[j] == 0:
                mem[j] = i
    return [mem[a] for a in A]


if __name__ == "__main__":
    main()
