def main():
    S = input()
    res = solve(S)
    print("Yes" if res else "No")


def solve(S):
    N = int(S[3:])
    return 1 <= N <= 349 and N != 316


if __name__ == "__main__":
    main()
