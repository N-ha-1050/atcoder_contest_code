def main():
    N = int(input())
    A = [int(a) - 1 for a in input().split()]
    W = [int(w) for w in input().split()]
    res = solve(N, A, W)
    print(res)


def solve(N, A, W):

    # box_cnt[i] := 箱iに入っている荷物の個数
    box_cnt = [0 for _ in range(N)]
    for a in A:
        box_cnt[a] += 1

    # 空の箱のうち最も小さいインデックス
    blank_box_idx = 0

    # 荷物が軽い順にインデックスを並び替える
    sorted_idx = sorted(range(N), key=lambda i: W[i])

    # 動かした合計重量
    res = 0

    # 荷物が軽い順にみる
    for idx in sorted_idx:

        # その荷物がどの箱に入っているのか
        a = A[idx]

        # 箱に一つしか入っていなければ次へ
        if box_cnt[a] == 1:
            continue

        # インデックスが最も小さい空の箱を探す
        while box_cnt[blank_box_idx] > 0:
            blank_box_idx += 1

        # 荷物idx を 箱a から 箱blank_box_idx に移す
        box_cnt[a] -= 1
        box_cnt[blank_box_idx] += 1
        A[idx] = blank_box_idx
        res += W[idx]
    return res


if __name__ == "__main__":
    main()
