import datetime, logging

def bisection_protocols(f, a: [int, float], b: [int, float], tolerance: [float]):
    assert(isinstance(a, (int, float)))
    assert(isinstance(b, (int, float)))
    assert(type(tolerance) == float)
    bisection_start = datetime.datetime.now()
    # - Failsafe 1 -
    if f(a) * f(b) > 0:
        return None, 0, []
    # - Failsafe 2 -
    if tolerance < 0:
        logging.error(f"Tolerance inputted: {tolerance}")
        logging.error("Tolerance is in the negatives. Negative tolerance is incompatible.")
        return None, 0, []

    iterations = 0
    errors_tracked = []
    while (b - a) / 2 > tolerance:
        c = (a + b) / 2
        errors_tracked.append(abs(f(c)))
        if f(c) == 0:
            return c, iterations, errors_tracked
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
        iterations += 1
    # -> Return <-
    bisection_end = datetime.datetime.now() - bisection_start
    logging.info(f"Bisection processing time: {bisection_end}")
    return (a + b)/2, iterations, errors_tracked

def newtons_method(f, df, x_0, tolerance: float, max_iterations: int):
    assert(type(x_0) == int or type(x_0) == float)
    assert(type(tolerance) == float)
    assert(type(max_iterations) == int)
    # - Time start timer -
    newtons_start = datetime.datetime.now()
    # - Failsafe 1 -
    if tolerance < 0:
        logging.error(f"Tolerance inputted: {tolerance}")
        logging.error("Tolerance is in the negatives. Negative tolerance is incompatible.")
        return None, 0, []

    errors_tracked = []
    iterations = 0
    x = x_0
    for _ in range(max_iterations):
        fx = f(x)
        errors_tracked.append(abs(fx))

        if abs(fx) < tolerance:
            return x, iterations, errors_tracked

        dfx = df(x)
        # - Divide by zero failsafe -
        if dfx == 0:
            return None, iterations, errors_tracked

        x = x - fx / dfx
        iterations += 1

    newtons_end = datetime.datetime.now() - newtons_start
    logging.info(f"Newtons method processing time: {newtons_end}")
    return x, iterations, errors_tracked