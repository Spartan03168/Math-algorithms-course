import random


def generate_linear_system_raw(n, value_range=(-10, 10)):
    """
    Generates a random linear system Ax = b with a known solution using raw Python lists.
    Each step is printed out for clarity.

    Parameters:
        n (int): The size of the system (n x n matrix).
        value_range (tuple): Range of integer values for the matrix elements.

    Returns:
        A (list of lists): The generated coefficient matrix.
        x (list): The known solution vector.
        b (list): The right-hand side vector.
    """
    # Step 1: Generate a random integer matrix A
    A = [[random.randint(value_range[0], value_range[1]) for _ in range(n)] for _ in range(n)]
    print("Generated matrix A:")
    for row in A:
        print(row)

    # Step 2: Define the known solution as x = [1, 2, ..., n]
    x = [[i + 1] for i in range(n)]
    print("\nKnown solution vector x:")
    for row in x:
        print(row)

    # Step 3: Compute the right-hand side vector b = Ax manually
    b = [[sum(A[i][j] * x[j][0] for j in range(n))] for i in range(n)]
    print("\nComputed right-hand side vector b:")
    for row in b:
        print(row)

    return A, x, b


# Example usage
n = 5  # Size of the system
A_raw, x_raw, b_raw = generate_linear_system_raw(n)
