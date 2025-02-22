def main():
    N = int(input())
    S = [input() for _ in range(N)]
    res = solve(N, S)
    print(res)


def solve(N: int, S: list) -> str:
    S.sort(key=len)
    return "".join(S)


if __name__ == "__main__":
    main()
