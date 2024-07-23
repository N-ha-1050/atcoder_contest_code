# CPython だと TLE(PyPy なら通る)

from more_itertools import distinct_permutations


def main():
    N, K = map(int, input().split())
    S = input()
    res = solve(N, K, S)
    print(res)


def solve(N, K, S):
    cnt = 0

    # S の並び替え(アナグラム)を重複無しで生成
    # itertools の permutation では間に合わない
    for T in distinct_permutations(S):

        # i := (回文の開始点)
        for i in range(N - K + 1):

            # 回分の判定
            for j in range(K // 2):
                if T[i + j] != T[i + K - j - 1]:

                    # 回文でなければ次のiへ
                    break
            else:

                # j についてループが終了した→回文が含まれていた
                # 次のTへ
                break
        else:

            # i についてループが終了した→回文が一つもなかった
            # カウントアップ
            cnt += 1
    return cnt


if __name__ == "__main__":
    main()
