def main():
    A = tuple(map(int, input().split()))
    B = tuple(map(int, input().split()))
    C = tuple(map(int, input().split()))
    res = solve(A, B, C)
    print("Yes" if res else "No")


def solve(A, B, C):
    # 各辺の二乗
    a2 = abs(B[0] - C[0]) ** 2 + abs(B[1] - C[1]) ** 2
    b2 = abs(C[0] - A[0]) ** 2 + abs(C[1] - A[1]) ** 2
    c2 = abs(A[0] - B[0]) ** 2 + abs(A[1] - B[1]) ** 2

    # 斜辺となりうる辺を探す
    # →斜辺となりうるのは最も長い辺
    x, y, z = sorted([a2, b2, c2])

    return x + y == z


if __name__ == "__main__":
    main()
