import random

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
# ------------------------------
print(f"\nKnown solutions: {x}")

# - Computation -
results = []
for outer_layer in range(length):
    sum_tracked = 0
    for internal_layer in range(length):
        sum_tracked += matrix[outer_layer][internal_layer] * x[internal_layer]
    results.append(sum_tracked)
# ------------------------------
print("Results from computation")
for res in results:
    print(res)

# - Forward gaussian elimination -
n = len(matrix)

for i in range(n):
    # -> Find non-zero pivot
    if matrix[i][i] == 0:
        for k in range(i + 1, n):
            if matrix[k][i] != 0:
                matrix[i], matrix[k] = matrix[k], matrix[i]
                results[i], results[k] = results[k], results[i]
                print(f"Swapped row {i} with row {k} to avoid zero pivot.")
                break
    pivot_tracked = matrix[i][i]
    if pivot_tracked == 0:
        raise ValueError(f"No nonzero pivot found in column {i}, system may be singular.")
    # -> Eliminate elements below pivot <-
    for j in range(i + 1, n):
        factor = matrix[j][i] / pivot_tracked
        for k in range(i, n):
            matrix[j][k] -= factor * matrix[i][k]
        results[j] -= factor * results[i]
        print(f"---\nFactor: {factor}")
        print(f"Row {j} was updated with {i}\n---")

# - Updated triangular matrix -
print(f"\nUpdated current triangular matrix")
for row in matrix:
    print(row)
# - Print updated right hand side vector -
print("\nUpdated right hand side vector")
for row_az2 in results:
    print(row_az2)