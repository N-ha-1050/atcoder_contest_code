def main():
    N, L, R = map(int, input().split())
    res = solve(N, L, R)
    print(*res)


def solve(N, L, R):
    # tuple や list は + 記号で連結できる
    return tuple(range(1, L)) + tuple(range(R, L - 1, -1)) + tuple(range(R + 1, N + 1))


if __name__ == "__main__":
    main()
