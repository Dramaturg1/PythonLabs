def find_digits_less5(str):
    count = 0
    for symb in str:
        if symb == '5':
            count+=1
    return count

def find_abscent_symbols(str):
    alph = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    arr = set([symb for symb in str])
    return sorted(alph - arr)

def find_digits_greater5(str):
    count = 0
    for symb in str:
        if symb in '6789':
            count+=1
    return count

print(find_digits_less5("842309rf5dhuf89ewch8534hdiw"))
print(find_abscent_symbols("wdjcheivuegcbuanlUHIWUFCJSDCUIISBDC"))
print(find_digits_greater5("uerfherufh348r029fu48h3"))