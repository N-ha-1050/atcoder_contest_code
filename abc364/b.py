def main():
    H, W = map(int, input().split())
    S = tuple(map(lambda x: int(x) - 1, input().split()))
    C = [input() for _ in range(H)]
    X = input()
    res = solve(H, W, S, C, X)
    print(*res)


def solve(H, W, S, C, X):
    ds = {"L": (0, -1), "R": (0, 1), "U": (-1, 0), "D": (1, 0)}

    def is_in(i, j):
        return 0 <= i < H and 0 <= j < W

    i, j = S
    for x in X:
        di, dj = ds[x]
        ni, nj = i + di, j + dj
        if not is_in(ni, nj):
            continue
        if C[ni][nj] == "#":
            continue
        i, j = ni, nj
    return i + 1, j + 1


if __name__ == "__main__":
    main()
