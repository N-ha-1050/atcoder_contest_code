def main():
    A = [int(a) for a in input().split()]
    res = solve(A)
    print("Yes" if res else "No")


def solve(A: list[int]):
    a, b, c = A
    return a * b == c or b * c == a or c * a == b


if __name__ == "__main__":
    main()
