from collections import deque


def main():
    N, M, K = map(int, input().split())
    A = [int(a) for a in input().split()]
    B = [int(b) for b in input().split()]
    res = solve(N, M, K, A, B)
    print(res)


def solve(N, M, K, A, B):
    # キューで管理する方法

    que = deque()  # A のうち読む本の時間を管理するキュー
    time, cnt = 0, 0  # time: 本を読むための合計時間, cnt: 読める冊数

    # A の本のみをできるだけ読む場合で初期化
    for a in A:
        if time + a > K:
            break
        time += a
        cnt += 1
        que.append(a)
    res = cnt

    # B を上から1冊ずつ読みながら A を減らす
    for b in B:

        # 1冊追加で読む
        time += b
        cnt += 1

        # 制限時間を超えていてAを読んでいるあいだAを減らす
        while que and time > K:
            a = que.pop()
            time -= a
            cnt -= 1

        # A を読まなくても制限時間が超えるとき終了
        if time > K:
            break

        # 最大冊数を更新
        res = max(res, cnt)

    return res


def solve2(N, M, K, A, B):
    # インデックスで管理する方法

    idxA = 0  # 半開区間 [0, idxA) 、 [0, idxB) の本を読む
    time = 0  # 本を読むための合計時間

    # A の本のみをできるだけ読む場合で初期化
    for a in A:
        if time + a > K:
            break
        time += a
        idxA += 1
    res = idxA

    # B を上から1冊ずつ読みながら A を減らす
    for idxB, b in enumerate(B, 1):

        # 1冊追加で読む
        time += b

        # 制限時間を超えていてAを読んでいるあいだAを減らす
        while time > K and idxA > 0:
            idxA -= 1
            time -= A[idxA]

        # A を読まなくても制限時間が超えるとき終了
        if time > K:
            break

        # 最大冊数を更新
        res = max(res, idxA + idxB)

    return res


if __name__ == "__main__":
    main()
