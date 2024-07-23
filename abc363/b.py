def main():
    N, T, P = map(int, input().split())
    L = [int(l) for l in input().split()]
    res = solve(N, T, P, L)
    print(res)


def solve(N, T, P, L):
    return max(T - sorted(L, reverse=True)[P - 1], 0)


if __name__ == "__main__":
    main()
