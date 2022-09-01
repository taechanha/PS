# 3:01 ~ 3:31 (21) 단순 구현

const = ""

a = "###.....###.#..####.#.......#.#....####.....###.#....##.#.......#.#....####.....###.#....#"
data = []
divide = len(a) // 5
new = ""
for i, ch in enumerate(a):
    if i != 0 and i % divide == 0:
        data.append(new)
        new = ""
    new += ch
data.append(new)
for row in data:
    print(row)
