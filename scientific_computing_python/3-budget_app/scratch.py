categories = ["food", "services", "household"]
max_len = max(len(x) for x in categories)
chart = ""
for index in range(0, max_len):
    for category in categories:
        if len(category) > index:
            chart += f' {category[index]} '
        else:
            chart += f'   '
    chart += "\n"
print(chart)
