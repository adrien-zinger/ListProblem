def read():
    # Don't let the machines win. You are humanity's last hope...
    width = int(input())  # the number of cells on the X axis
    height = int(input())  # the number of cells on the Y axis
    lines = []
    nodes = []
    for i in range(height):
        line = input()  # width characters, each either 0 or .
        lines.append(line)
        for j, c in enumerate(line):
            if c == '0':
                nodes.append((j, i))
    return (width, height, lines, nodes)

def compute(x, y, w, h, lines):
    nexts = [(-1, -1), (-1, -1)]
    for nx in range(x + 1, w):
        if lines[y][nx] == '0':
            nexts[0] = (nx, y)
            break
    for ny in range(y + 1, h):
        if lines[ny][x] == '0':
            nexts[1] = (x, ny)
            break
    return nexts

def push(nodes, nexts, computed):
        for n in nexts:
            if n[0] != -1 and n[1] != -1 and not n in computed and not n in nodes:
                nodes.append(n)
        return nodes

def outputs(width, height, lines, nodes):
    computed = []
    curr = nodes.pop(0)
    nexts = compute(*curr, width, height, lines)
    computed.append(curr)
    nodes = push(nodes, nexts, computed)
    yield (curr, nexts)
    while len(nodes) != 0:
        curr = nodes.pop(0)
        nexts = compute(*curr, width, height, lines)
        computed.append(curr)
        nodes = push(nodes, nexts, computed)
        yield (curr, nexts)

if __name__ == "__main__":
    for i, (n, nexts) in enumerate(outputs(*read())):
        print(f"{n[0]} {n[1]} {nexts[0][0]} {nexts[0][1]} {nexts[1][0]} {nexts[1][1]}")
