def main():
    S1, S2 = input().split()
    res = solve(S1, S2)
    print(res)


def solve(S1: str, S2: str) -> int:
    All = {1, 2, 3, 4}
    Takahashi = {1, 2}
    Aoki = {1, 3}

    if S1 == "fine":
        Takahashi = All - Takahashi
    if S2 == "fine":
        Aoki = All - Aoki
    return (Takahashi & Aoki).pop()


if __name__ == "__main__":
    main()
