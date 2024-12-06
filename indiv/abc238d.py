def main():
    T = int(input())
    for _ in range(T):
        a, s = map(int, input().split())
        res = solve(a, s)
        print("Yes" if res else "No")


def solve(a: int, s: int):
    return s >= 2 * a and (s - 2 * a) & a == 0


if __name__ == "__main__":
    main()
