"""Найти кол-во счастливых билетов в 1 серии."""
total = 0
for x in range(1000):
    for y in range(1000):
        first_half = x//100 + (x % 100)//10 + x % 10
        second_half = y//100 + (y % 100)//10 + y % 10
        if first_half == second_half:
            total += 1
total -= 1  # except equation 0 = 0
print('Amount of happy tickets is %d' % total)