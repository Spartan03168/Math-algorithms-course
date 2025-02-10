import datetime, logging, re
import sympy as sp
import streamlit as st

def parser(formula, testing_mode):
    # - Valid function failsafe -
    if not formula.strip():
        if testing_mode != 1:
            st.error("Error: Please enter a valid function before running the solver.")
        elif testing_mode == 1:
            raise ValueError("Equation is empty. Please enter a valid function.")
        return None, None
    else:
        formula = re.sub(r"(\d)([a-zA-Z])", r"\1*\2", formula.strip())

    print("Parser in progress...")
    try:
        x = sp.symbols("x")
        expression = sp.sympify(formula)
        lambda_conversion = sp.lambdify(x, expression, "numpy")
        primed = sp.lambdify(x, sp.diff(expression, x), "numpy")
        return lambda_conversion, primed
    except Exception as e:
        error_message = f"Failed to parse equation: '{formula}'. Error: {e}"
        if testing_mode != 1:
            st.error(error_message)
        elif testing_mode == 1:
            print(error_message)
        raise ValueError(error_message)

def bisection_protocols(f, a: [int, float], b: [int, float], tolerance: [float], testing_mode: int):
    assert(isinstance(a, (int, float)))
    assert(isinstance(b, (int, float)))
    assert(type(tolerance) == float)
    bisection_start = datetime.datetime.now()
    print("Bijection calculations in progress...")

    # - Failsafe 1 -
    if f(a) * f(b) > 0:
        if testing_mode == 1:
            print(f"Invalid interval: f(a) and f(b) must have opposite signs.")
        else:
            st.error(
                "Error: Bisection method requires f(a) and f(b) to have opposite signs. Please enter a valid interval.")
        return None, 0, []
    # - Failsafe 2 -
    if tolerance < 0:
        if testing_mode == 1:
            print(f"Invalid interval: f(a) and f(b) must have opposite signs.")
        else:
            st.error(
                "Error: Bisection method requires f(a) and f(b) to have opposite signs. Please enter a valid interval.")
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
    if testing_mode == 1:
        pass
    else:
        pass
    return (a + b)/2, iterations, errors_tracked

def newtons_method(f, df, x_0, tolerance: float, max_iterations: int, testing_mode: int):
    assert(type(x_0) == int or type(x_0) == float)
    assert(type(tolerance) == float)
    assert(type(max_iterations) == int)
    # - Time start timer -
    newtons_start = datetime.datetime.now()
    print("Newtons method calculations in progress...")
    # - Failsafe 1 -
    if tolerance < 0:
        if testing_mode == 1:
            pass
        else:
            pass

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