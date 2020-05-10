def permutation(s):
    if len(s) == 1:
        return [s]
    elif len(s) == 0:
        return [s]

    perm_list = []
    for a in s:
        elements = [x for x in s if x != a]
        z = permutation(elements)
        for t in z:
            perm_list.append([a] + t)

    return perm_list


n = int(input("Введите число = "))
myarr = [i + 1 for i in range(n)]

for line in permutation(myarr):
    print(line)
