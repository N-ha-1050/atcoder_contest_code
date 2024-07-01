def main():
    N, A = map(int, input().split())
    T = [int(t) for t in input().split()]
    res = solve(N, A, T)
    print(*res, sep="\n")


def solve(N, A, T):
    now = 0
    res = []
    for t in T:
        now = max(now, t) + A
        res.append(now)
    return res


if __name__ == "__main__":
    main()
