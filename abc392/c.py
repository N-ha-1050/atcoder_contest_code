def main():
    N = int(input())
    P = [int(p) - 1 for p in input().split()]
    Q = [int(q) - 1 for q in input().split()]
    res = solve(N, P, Q)
    print(*res)


def solve(N: int, P: list[int], Q: list[int]):
    S = [-1 for _ in range(N)]
    for p, q in zip(P, Q):
        S[q] = Q[p]
    return [s + 1 for s in S]


if __name__ == "__main__":
    main()
