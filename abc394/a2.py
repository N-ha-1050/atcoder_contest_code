def main():
    S = input()
    res = solve(S)
    print(res)


def solve(S: str) -> str:
    return "2" * S.count("2")


if __name__ == "__main__":
    main()
