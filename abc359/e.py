from collections import deque


def main():
    N = int(input())
    H = [int(h) for h in input().split()]
    res = solve(N, H)
    print(*res)


def solve(N, H):

    # 答えを記録
    res = []

    # deq[i] := (開始点, 幅, 高さ) (以下、まとめて「情報」)
    deq = deque()

    # 合計到達時間の記録
    t = 1

    # Hを順番に見る
    for i, h in enumerate(H):

        # 開始点の初期値として現在地を設定
        s = i

        # 過去のものを直近から遡る
        while deq:

            # その時点での情報を取得
            ps, pw, ph = deq.pop()

            # 現在の高さのほうが小さければ、もとに戻してそれ以上は見ない
            if h < ph:
                deq.append((ps, pw, ph))
                break

            # 合計時間からその時点の分を引く
            t -= pw * ph

            # 開始点を更新
            s = ps

        # 幅を求める
        w = i - s + 1

        # 現在の情報を追加
        deq.append((s, w, h))

        # 合計時間に現在の分を追加
        t += w * h

        # 答えに現在までの合計時間を追加
        res.append(t)

    return res


if __name__ == "__main__":
    main()
