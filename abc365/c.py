def main():
    N, M = map(int, input().split())
    A = [int(a) for a in input().split()]
    res = solve(N, M, A)
    print("infinite" if res is None else res)


def solve(N, M, A):
    cum = 0
    for i, a in enumerate(sorted(A)):
        if cum + a * (N - i) > M:
            return (M - cum) // (N - i)
        cum += a
    return None


if __name__ == "__main__":
    main()
