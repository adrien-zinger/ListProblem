# This is the code I found on the website after solving the problem
# I didn't write this but I want to be able to think like this later

w, h = int(input()), int(input())
h = [input() for _ in range(h)]

# This is a very interesting method to get the verticals lists
# the star will split the lines in multiple values.
# Go to the test_solution2 file the look at a basic usecase of this process
v = [''.join(x) for x in zip(*h)]

# Then for each (x, y)
for y, line in enumerate(h):
    for x, p in enumerate(line):
        if p == '0':
            x1 = line.find('0', x + 1)
            y2 = v[x].find('0', y + 1)
            print(' '.join(map(str, (
                x, y,
                x1, -1 if x1 == -1 else y,
                -1 if y2 == -1 else x, y2
            ))))