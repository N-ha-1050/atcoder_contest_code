def main():
    N, X, Y, Z = map(int, input().split())
    res = solve(N, X, Y, Z)
    print("Yes" if res else "No")


def solve(N, X, Y, Z):
    return min(X, Y) < Z < max(X, Y)


if __name__ == "__main__":
    main()
