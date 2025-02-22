def main():
    S = list(input())
    res = solve(S)
    print(res)


def solve(S: list[str]) -> str:
    N = len(S)
    for i in reversed(range(N - 1)):
        if S[i] == "W" and S[i + 1] == "A":
            S[i], S[i + 1] = "A", "C"
    return "".join(S)


if __name__ == "__main__":
    main()
