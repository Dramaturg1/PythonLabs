from collections import defaultdict

data = []
while True:
    line = input().strip()
    if line == '':
        break
    data.append(line)
sales = defaultdict(lambda: defaultdict(int))

for line in data:
    parts = line.split()
    customer = parts[0]
    product = parts[1]
    quantity = int(parts[2])
    sales[customer][product] += quantity

sorted_customers = sorted(sales.keys())

for customer in sorted_customers:
    print(f"{customer}:")
    sorted_products = sorted(sales[customer].items())
    for product, total in sorted_products:
        print(f"{product} {total}")