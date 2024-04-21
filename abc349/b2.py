import collections


def main():
    S = input()
    res = solve(S)
    print("Yes" if res else "No")


def solve(S):
    # ex: S = commencement

    # collections の Counter 型 は、文字列やリストなどから、要素とその出現回数を記録できます。
    # dict 型とほぼ同じように扱えます(サブクラスです)。
    #
    # https://note.nkmk.me/python-collections-counter/#collectionscounter

    cnt = collections.Counter(S)
    # cnt = {'m': 3, 'e': 3, 'c': 2, 'n': 2, 'o': 1, 't': 1}

    mem = collections.Counter(cnt.values())
    # mem = {2: 2, 1: 2, 3: 2}

    for value in mem.values():
        if value != 2:
            return False

    return True


if __name__ == "__main__":
    main()
