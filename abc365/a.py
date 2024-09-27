def main():
    Y = int(input())
    res = solve(Y)
    print(res)


def solve(Y):
    if Y % 4 != 0:
        return 365
    elif Y % 100 != 0:
        return 366
    elif Y % 400 != 0:
        return 365
    else:
        return 366


if __name__ == "__main__":
    main()
