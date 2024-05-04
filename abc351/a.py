def main():
    A = [int(a) for a in input().split()]
    B = [int(b) for b in input().split()]
    res = solve(A, B)
    print(res)


def solve(A, B):
    return sum(A) - sum(B) + 1


if __name__ == "__main__":
    main()
