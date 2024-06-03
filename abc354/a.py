def main():
    H = int(input())
    res = solve(H)
    print(res)


def solve(H):

    # res 日目の朝に height cm
    height = 0
    res = 0

    while height <= H:
        height += 2**res
        res += 1
    return res


if __name__ == "__main__":
    main()
