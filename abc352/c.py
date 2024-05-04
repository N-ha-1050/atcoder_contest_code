def main():
    N = int(input())
    AB = [tuple(map(int, input().split())) for _ in range(N)]
    res = solve(N, AB)
    print(res)


def solve(N, AB):
    return max(b - a for a, b in AB) + sum(a for a, _ in AB)


if __name__ == "__main__":
    main()
