import re

def find_dates(text):
    pattern = r'\b(0?[1-9]|[12][0-9]|3[01])\s+(января|февраля|марта|апреля|мая|июня|июля|августа|сентября|октября|ноября|декабря)\s+(\d{4})\b'
    return re.findall(pattern, text)

dates = find_dates("вовлыовытос 12 января 1997 13 сентябрь овцарлав 24 сентября 2002")
for day, month, year in dates:
    print(f"{day} {month} {year}")