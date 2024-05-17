def main():
    N, K = map(int, input().split())
    A = [int(a) for a in input().split()]
    res = solve(N, K, A)
    print(res)


def solve(N, K, A):
    res = 0  # スタートした回数
    cnt = 0  # 現在の乗車人数

    for a in A:  # すべてのグループについて
        if K - cnt < a:  # 空き席がグループの人数より少ないとき
            res += 1  # スタートさせて
            cnt = 0  # すべて空席にする
        cnt += a  # グループを乗車させる
    else:  # 最後のグループが乗車したら
        res += 1  # スタートさせる

    return res


if __name__ == "__main__":
    main()
