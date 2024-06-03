def main():
    N = int(input())
    AB = [tuple(map(int, input().split())) for _ in range(N)]
    res = solve(N, AB)
    print("Takahashi" if res else "Aoki")


def solve(N, AB):
    # メモ用リスト
    mem = [None for _ in range(1 << N)]

    # メモ化再帰
    def dfs(field=0):
        # field: 二進数表記した field の i桁目 が1のとき、i番目のカードが使われている場の状況、場の状況が等しい場合答えも常に等しい

        # すでに見ていたら、その時の値を返す
        if mem[field] is not None:
            return mem[field]

        # 使っていないカードを2枚選ぶ
        for i in range(N):
            if field >> i & 1:
                continue
            for j in range(i + 1, N):
                if field >> j & 1:
                    continue

                # 選んだ2枚を捨てられるとき
                if AB[i][0] == AB[j][0] or AB[i][1] == AB[j][1]:
                    # field を更新して次の人へ
                    field += 1 << i
                    field += 1 << j
                    res = dfs(field)
                    field -= 1 << i
                    field -= 1 << j

                    # 次の場で先手が勝てない(= 後手必勝)なら、この場では先手が必勝
                    if not res:
                        mem[field] = True
                        return True

        # どの次の場でも先手必勝(= 後手が勝てない)場合、この場では先手が必勝
        mem[field] = False
        return False

    res = dfs()
    return res


if __name__ == "__main__":
    main()
