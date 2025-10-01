import collections

def stats(text):
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

def task11():
    lines = []
    while True:
        line = input().strip()
        if not line:
            break
        lines.append(line)
    print(sorted(lines, key=calculate))

def calculate_global_frequencies(lines):
    if not lines:
        return {}
    all_text = ''.join(lines)  
    if not all_text:
        return {}
    global_counter = collections.Counter(all_text)
    total_chars = len(all_text)
    global_freq = {char: count / total_chars for char, count in global_counter.items()}  
    return global_freq

def task12(lines):
    global_freq = calculate_global_frequencies(lines)
    lines_with_info = []
    for line in lines:
        if not line:
            lines_with_info.append((line, 0.0, '', 0.0, 0.0))
            continue 
        line_counter = collections.Counter(line)
        most_common_char, line_count = line_counter.most_common(1)[0]
        line_frequency = line_count / len(line)
        global_frequency = global_freq.get(most_common_char, 0)
        deviation = (line_frequency - global_frequency) ** 2
        lines_with_info.append((line, deviation, most_common_char, line_frequency, global_frequency))
    lines_with_info.sort(key=lambda x: x[1]) 
    return lines_with_info

def calculate_mirror_pairs_diff(line):
    if not line:
        return 0.0
    n = len(line)
    total_diff = 0
    pair_count = 0
    for i in range(n // 2):
        left_char = line[i]
        right_char = line[n - 1 - i]
        diff = abs(ord(left_char) - ord(right_char))
        total_diff += diff
        pair_count += 1
    if pair_count == 0:
        return 0.0
    
    return total_diff / pair_count

def calculate_deviation(line):
    if not line:
        return 0.0
    max_ascii = max(ord(char) for char in line)
    mirror_diff = calculate_mirror_pairs_diff(line)
    deviation = (max_ascii - mirror_diff) ** 2  
    return deviation

def task13(lines):
    return sorted(lines, key=lambda line: calculate_deviation(line))

def count_mirror_triples(line):
    if len(line) < 3:
        return 0.0   
    mirror_count = 0
    total_positions = len(line) - 2
    for i in range(len(line) - 2):
        if line[i] == line[i + 2]:
            mirror_count += 1   
    return mirror_count / total_positions if total_positions > 0 else 0.0

def task14(lines):
    return sorted(lines, key=lambda line: count_mirror_triples(line))

#тест 14
'''
test_lines = [
    "abc",         
    "abcd",          
    "aba",           
    "abacaba",       
    "aaa",           
    "aabaa",        
    "level",         
    "radar",        
    "12321",         
    "abcba",         
    "x",             
    "xy",            
    "",             
    "abada",         
    "mirror",        
]
    
sorted_lines = task14(test_lines)
    
for line in sorted_lines:
    avg_triples = count_mirror_triples(line)
    triples_list = []
    if len(line) >= 3:
        for i in range(len(line) - 2):
            triple = line[i:i+3]
            if line[i] == line[i + 2]:
                triples_list.append(triple)  
    triples_str = ", ".join(triples_list) if triples_list else "нет"       
    print(f"Ср. кол-во: {avg_triples:.4f} | "
            f"Тройки: {triples_str:15} | "
            f"Длина: {len(line):2d} | "
            f"Строка: '{line}'")
'''
#тест 13
'''
test_lines = [
    "abcba",     
    "abcde",      
    "ABCDE",      
    "a",         
    "ab",         
    "abc",        
    "hello",     
    "radar",      
    "level",      
    "12321",      
    "",           
    "Aa",        
    "!@#$%",      
]  
sorted_lines = task13(test_lines)     
for line in sorted_lines:
    if line:
        max_ascii = max(ord(char) for char in line)
        mirror_diff = calculate_mirror_pairs_diff(line)
        deviation = calculate_deviation(line)
        n = len(line)
        pairs_info = []
        for i in range(n // 2):
            left = line[i]
            right = line[n - 1 - i]
            diff = abs(ord(left) - ord(right))
            pairs_info.append(f"'{left}'-'{right}'(diff:{diff})")           
        pairs_str = " | ".join(pairs_info) if pairs_info else "нет пар"          
        print(f"Отклонение: {deviation:8.2f} | "
                f"Макс.ASCII: {max_ascii:3d} | "
                f"Разница пар: {mirror_diff:6.2f} | "
                f"Пары: {pairs_str:20} | "
                f"Строка: '{line}'")
    else:
        print(f"Отклонение: {0:8.2f} | Макс.ASCII: {0:3d} | Разница пар: {0:6.2f} | Пары: {'пустая строка':20} | Строка: ''")
'''
#тест 12го номера
'''
test_lines = [
    "ааааа бб вв",
    "ооооо пп рр",
    "программирование",
    "частотный анализ",
    "xxx yyy zzz",
]
detailed_sorted = task12(test_lines) 
for line, deviation, char, line_freq, global_freq in detailed_sorted:
    if line:
        print(f"Откл: {deviation:.6f} | Символ: '{char}' | "
                f"В строке: {line_freq:.3f} | Глобально: {global_freq:.3f} | "
                f"Строка: '{line}'")
'''