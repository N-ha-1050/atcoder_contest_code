import bisect


def main():
    X = int(input())
    res = solve(X)
    print(res)


def solve(X: int) -> int:
    # 100未満ならその値が答え
    if X < 100:
        return X

    # 100以上なら、等差数を小さい順に列挙していく
    nums = [i for i in range(11, 100)]
    i = 0
    while True:
        n = nums[i]
        i += 1
        a = n % 10  # 一の位
        b = n // 10 % 10  # 十の位
        d = a + (a - b)  # 次の桁
        if not (0 <= d < 10):
            continue
        k = n * 10 + d

        # X以上なら答え
        if k >= X:
            return k

        nums.append(k)
    return -1


if __name__ == "__main__":
    main()
