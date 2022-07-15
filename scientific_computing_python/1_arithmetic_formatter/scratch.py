def printout(category):
    cat_len = len(category)

    cat_right = int(cat_len / 2)
    cat_left = int(cat_len /2) if cat_len % 2 == 0 else int(cat_len / 2 + 1)

    output = (
        f'{"*" * (15 - cat_left)}'
        f'{category[0:cat_left]}'
        f'{category[cat_left:]}'
        f'{"*" * (15 -cat_right)}'
        )
    return output

a1 = printout("hello")
print(a1)
print(len(a1))
a2 = a1.split('h')
a3 = a1.split('o')
print(a2, a3, len(a2[0]), len(a3[-1]))


