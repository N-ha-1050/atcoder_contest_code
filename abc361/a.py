def main():
    N, K, X = map(int, input().split())
    A = [int(a) for a in input().split()]
    res = solve(N, K, X, A)
    print(*res)


def solve(N, K, X, A):
    A.insert(K, X)
    return A


if __name__ == "__main__":
    main()
