def main():
    R = int(input())
    res = solve(R)
    print(res)


def solve(R):
    return 100 - R % 100


if __name__ == "__main__":
    main()
