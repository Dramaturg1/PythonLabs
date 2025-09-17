import math

def count_even_non_prime_nums(x):
	if x % 2 == 0:
		return x/2
	else:
		count = 0
		for i in range (2, x, 2):
			if Math.gcd(x, i) == 1
				count+=1
		return count

def max_non_three_digit(x):
	max_digit = -1
	x = abs(x)
	while x != 0:
		max_digit = max(max_digit, x % 10)
		x //= 10
	return max_digit

def find_min_divisor(x):
	if x <= 1 return None
	min_divisor = None
	for i in range(2, int(x**0.5)):
		if x % i == 0:
			if i > min_divisor:
				min_divisor = i
	return min_divisor

def sum_of_digits(x):
	summ = 0
	while x > 0:
		if (x % 10) < 5:
			summ+= x % 10
		x//= 10
	return summ

def product_method(x):
	x = abs(x)
	if x <= 1 return None
	divisor = find_min_divisor(x)
	dig_sum = sum_of_digits(x)
	for i in range (x-1, 2, -1):
		if Math.gcd(x, i) != 1 and i % divisor != 0:
			return dig_sum * i
	return None

print(count_even_non_prime_nums(100), count_even_non_prime_nums(47))
print(max_non_three_digit(239213))
print(product_method(150))

