def main():
    A, B, C, D = map(int, input().split())
    res = solve(A, B, C, D)
    print(res)


def solve(A, B, C, D):

    # 第一象限に移動
    dx = -(A // 4) * 4
    A += dx
    C += dx

    dy = -(B // 4) * 4
    B += dy
    D += dy

    # 2次元累積和
    w, h = 4, 2
    cum = [
        [0, 0, 0],
        [0, 2, 3],
        [0, 3, 6],
        [0, 3, 7],
        [0, 4, 8],
    ]

    def get(x, y):
        # (A, B, C, D) = (0, 0, x, y) での答えを求める

        r = 0

        # 単位領域が何単位分あるか
        qx, rx = x // w, x % w
        qy, ry = y // h, y % h

        # 累積和で加算
        r += cum[w][h] * qx * qy
        r += cum[rx][h] * qy
        r += cum[w][ry] * qx
        r += cum[rx][ry]

        return r

    return get(C, D) - get(A, D) - get(C, B) + get(A, B)


if __name__ == "__main__":
    main()
