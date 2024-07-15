from collections import deque


def main():
    N = int(input())
    S = input()
    T = input()
    res = solve(N, S, T)
    print(res)


def solve(N, S, T):

    # 状態を3進数で管理する
    # Xの3進数表記i桁目でマスiの状態を表す
    # 0のとき.、1のときB、2のときW とする

    # S と T の状態をそれぞれ3進数に直す
    st = sum((1 if s == "B" else 2) * (3**i) for i, s in enumerate(S))
    gl = sum((1 if t == "B" else 2) * (3**i) for i, t in enumerate(T))

    # mem[state] := (状態stateに到達可能か)
    mem = [False for _ in range(3 ** (N + 2))]

    # deq[i] := (state, blank, step)
    # 状態state(マスblank, blank + 1 が空きマス)にstepで到達可能
    deq = deque([(st, N, 0)])

    while deq:
        now, blank, step = deq.popleft()

        # すでに到達可能な場合スキップ
        if mem[now]:
            continue

        # ゴールの場合 step を返す
        if now == gl:
            return step

        # 到達可能と記録する
        mem[now] = True

        # 次への遷移
        for i in range(N + 1):
            # マスiとi + 1を空きマスにしたい

            # 現在の空きマスと被ったら遷移不可能
            if i == blank or i == blank + 1 or i + 1 == blank:
                continue

            # a := i桁目の値
            a = now
            for _ in range(i):
                a //= 3
            a %= 3

            # b := i + 1桁目の値
            b = now
            for _ in range(i + 1):
                b //= 3
            b %= 3

            # 遷移先の状態
            nx = now - a * 3**i - b * 3 ** (i + 1) + a * 3**blank + b * 3 ** (blank + 1)

            # すでに遷移可能だと分かっていたらスキップ
            if mem[nx]:
                continue

            # キューに追加
            deq.append((nx, i, step + 1))

    # 到達不可能な場合 -1 を返す
    return -1


if __name__ == "__main__":
    main()
