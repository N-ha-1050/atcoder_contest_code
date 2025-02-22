def main():
    S = input()
    res = solve(S)
    print(res)


def solve(S: str) -> str:
    return "".join(s for s in S if s == "2")


if __name__ == "__main__":
    main()
