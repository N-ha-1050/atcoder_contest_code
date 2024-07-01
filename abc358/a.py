def main():
    S, T = input().split()
    res = solve(S, T)
    print("Yes" if res else "No")


def solve(S, T):
    return S == "AtCoder" and T == "Land"


if __name__ == "__main__":
    main()
