"""Найти кол-во счастливых билетов в 1 серии."""


total = 0
for x in range(1, 28):
    result = 0
    for y in range(1000):
        if y//100 + (y % 100)//10 + y % 10 == x:
            result += 1
    total += result**2
print('Amount of happy tickets is %d' % total)
