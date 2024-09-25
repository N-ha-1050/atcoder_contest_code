def main():
    N = int(input())
    S = [input() for _ in range(N)]
    res = solve(N, S)
    print("Yes" if res else "No")


def solve(N, S):
    for s1, s2 in zip(S, S[1:-1]):
        if s1 == s2 == "sweet":
            return False
    return True


if __name__ == "__main__":
    main()
