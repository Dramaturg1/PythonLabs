def stats(text)
    vowels = 'уеыаоэяию'
    cons = 'йцкнгшщзхфвпрлджчсмтб'
    v_count = 0
    c_count = 0
    letters = 0
    for symb in text.lower():
        if symb in vowels:
            v_count+= 1
            letters+= 1
        elif symb in cons:
            c_count+= 1
            letters+= 1
    return v_count, c_count, letters

def calculate(text):
    v_count, c_count, let_count = stats(text)
    if let_count == 0:
        return 0
    avg_vowels = v_c / let_count
    avg_cons = c_count / let_count
    return avg_cons - avg_vowels

lines = []

while True:
    line = input().strip()
    if not line:
        break
    lines.append(line)

print(sorted(lines, key=calculate))