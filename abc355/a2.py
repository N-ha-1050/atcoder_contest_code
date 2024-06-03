def main():
    A, B = map(int, input().split())
    res = solve(A, B)
    print(res)


def solve(A, B):
    return -1 if A == B else A ^ B


if __name__ == "__main__":
    main()
