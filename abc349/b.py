def main():
    S = input()
    res = solve(S)
    print("Yes" if res else "No")


def solve(S):
    # cnt[文字] := 出現回数
    cnt = {}
    for s in S:
        cnt[s] = cnt.get(s, 0) + 1

    # mem[出現回数] := 文字の種類数
    mem = {}
    for v in cnt.values():
        mem[v] = mem.get(v, 0) + 1

    # 判定： 種類数が 0 でも 2 でもないものが1つでもあれば即False
    for v in mem.values():
        if v != 2 and v != 0:
            return False
    return True


if __name__ == "__main__":
    main()
