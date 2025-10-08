n, k = map(int, input().split())
parties = []
for _ in range(k):
    a, b = map(int, input().split())
    parties.append((a, b))
strikes = set()
for a, b in parties:
    day = a
    while day <= n:
        weekend = (day -1) % 7 + 1
        if weekend != 6 and weekend != 7:
            strikes.add(day)
        day+=b
print(len(strikes))


