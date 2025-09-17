def isPalindrome(x):
    return x == x[::-1]

def count_words(x):
    return len(x.split())

def count_diff_digits(x):
    a = []
    while x > 0:
        a.append(x % 10)
        x//= 10
    return len(set(a))

print(isPalindrome("abcba"))
print(count_words("Pipi pipi popo popo popo ppopo ppp"))
print(count_diff_digits(123444444))