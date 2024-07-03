def main():
    N, T = map(int, input().split())
    S = input()
    X = [int(x) for x in input().split()]
    res = solve(N, T, S, X)
    print(res)


def solve(N, T, S, X):

    # pos: 正の方向に動く蟻の初期位置
    # neg: 負の方向に動く蟻の初期位置
    pos, neg = [], []
    for i in range(N):
        if S[i] == "0":
            neg.append(X[i])
        elif S[i] == "1":
            pos.append(X[i])

    # それぞれ小さい順に並び替える
    pos.sort()
    neg.sort()

    len_neg = len(neg)

    # 正の方向に動く初期位置がpの蟻と負の方向に動く初期位置がnの蟻がすれ違うか
    def is_cross(p, n):
        p_s, p_e = p, p + T
        n_s, n_e = n, n - T

        # p_s <= x <= p_e かつ n_e <= x <= n_s となる x が存在するかの判定
        # 一般に閉区間[s1, e1]と[s2, e2]に共通区間があることの判定は max(s1, s2) <= min(e1, e2) でできる
        return max(p_s, n_e) <= min(p_e, n_s)
        return p_s <= n_s and n_e <= p_e

    # 負の方向に進む蟻のうちすれ違う蟻の開始インデックスと終了インデックス
    neg_st, neg_ed = 0, 0

    # 合計ペア数
    res = 0

    # 正の方向に進む蟻について
    for p in pos:

        # pより大きい位置にいる蟻のうち最も小さい位置のインデックスを求める(neg_st が存在するならこの値)
        while neg_st < len_neg and neg[neg_st] < p:
            neg_st += 1

        # pより大きい位置にいる蟻がいなかった場合、それ以降のすべての蟻についてもすれ違う蟻は存在しないので終了
        if neg_st >= len_neg:
            break

        # p と neg[neg_st] がすれ違わない場合、これより大きい位置にいる蟻も p の位置の蟻とすれ違わない
        if not is_cross(p, neg[neg_st]):
            continue

        # 最も大きい位置にいるpの位置にいる蟻とすれ違う場合の数を求める
        neg_ed = max(neg_ed, neg_st)
        while neg_ed < len_neg and is_cross(p, neg[neg_ed]):
            neg_ed += 1

        #  区間[neg_st, neg_ed) に含まれる左向き蟻の数を合計に加算
        res += neg_ed - neg_st

    return res


if __name__ == "__main__":
    main()
