lines = []

while True:
    line = input().strip()
    if not line:
        break
    lines.append(line)

sorted_lines = sorted(lines, key= lambda x: len(x.split()))
print(sorted_lines)