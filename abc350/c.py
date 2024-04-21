def main():
    N = int(input())
    A = [int(a) - 1 for a in input().split()]
    res = solve(N, A)
    print(len(res))
    for i, j in res:
        print(i + 1, j + 1)


def solve(N, A):
    # pos[a] := (aの位置)
    pos = [None for _ in range(N)]
    for i, a in enumerate(A):
        pos[a] = i

    res = []
    for i in range(N):
        # 揃っていたら次へ
        if A[i] == i:
            continue

        # j := (i のある位置)
        j = pos[i]

        # swap(交換)
        A[i], A[j] = A[j], A[i]  # A[j] == i

        # pos の更新
        pos[A[i]] = i
        pos[A[j]] = j

        # res に追加
        res.append((i, j))
    return res


if __name__ == "__main__":
    main()
