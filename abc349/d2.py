def main():
    L, R = map(int, input().split())
    res = solve(L, R)
    print(len(res))
    for l, r in res:
        print(l, r)


def solve(L, R):
    # 左右それぞれから記録する
    res_l = []
    res_r = []

    # 見ている桁
    i = 0

    while L < R:
        if (L >> i) & 1:
            pre_L = L
            L += 1 << i
            res_l.append((pre_L, L))
        if (R >> i) & 1:
            pre_R = R
            R -= 1 << i
            res_r.append((R, pre_R))
        i += 1

    res = res_l + res_r[::-1]

    return res


if __name__ == "__main__":
    main()
