import statistics
import random
import math

nums = [random.randint(1, 100) for x in range(100)]

print("Медиана ->", statistics.median(nums))
print("Среднее значение ->", statistics.mean(nums))
print("Стандартное отклонение ->", round(statistics.stdev(nums), 2))
print("Округлённое значение корня суммы чисел ->", round(math.sqrt(sum(nums)), 2))
