import datetime

n = 100000
res = 100
h = res / n

loop_start_time = datetime.datetime.now()
x = float(0.0)
for i in range(n):
    x += h
loop_end_time = datetime.datetime.now()

print(f"Loop processing time: {loop_end_time - loop_start_time}")
print(f"h: {h}")
print(x)
print(x == res)
