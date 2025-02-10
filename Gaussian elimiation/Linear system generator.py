import random, datetime

start_time = datetime.datetime.now()
length = 5
# - Matrix fabrication -
value_options = [-15, 15]
matrix = [[random.randint(value_options[0], value_options[1]) for element in range(length)] for rows in range(length)]
print(f"-> {length} by {length} matrix <-")
for row in matrix:
    print(row)

# - Known solution -
x = []
for i in range(length):
    x.append(i + 1)
print(f"\nKnown solutions: {x}")

# - Computation -
results = []
for outer_layer in range(length):
    sum_tracked = 0
    for internal_layer in range(length):
        sum_tracked += matrix[outer_layer][internal_layer] * x[internal_layer]
    results.append(sum_tracked)

print("Results from computation")
for res in results:
    print(res)

# - End processing time -
end_time = datetime.datetime.now()
print(f"\nProcessing time: {end_time}")