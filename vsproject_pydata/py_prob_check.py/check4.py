# 문제 4

data = [
    ["open", "high", "low", "close"],
    [1000, 1200, 800, 1000],
    [1500, 1600, 800, 1400],
    [1400, 1700, 900, 1500],
    [2000, 25000, 1800, 2100]
]

for row in data[1:]:
    close_price = row[3]
    if close_price > 1500:
        print(close_price)
        