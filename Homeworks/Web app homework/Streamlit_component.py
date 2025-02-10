import streamlit as st
import matplotlib.pyplot as plt
from Backend import Backend_deployment

# - Behavior mods -
developer_mode = 1
testing_mode = 1
web_deployment = 1

# ----> Web deployment <----
if web_deployment == 1:
    if testing_mode != 1:
        st.title("Root finding web app assignment")
    a = int(input("a: ")) if testing_mode == 1 else st.number_input("Interval start (a): ", value=-10.0)
    b = int(input("b: ")) if testing_mode == 1 else st.number_input("Interval end (b): ", value=10.0)
    if testing_mode == 1:
        if a > b:
            print("a is bigger than be. This is compatible. a has to be smaller.")
            while(a > b):
                a = int(input("a: "))
                b = int(input("b: "))
    iterations_cnt = int(input("Iterations to test: ")) if testing_mode == 1 else st.number_input("Max iterations: ", value=100, step=10)
    formula = input("Enter function (Example format, x**2 - 5*sin(x) + x - 1): ") if testing_mode == 1 else st.text_input("Enter function (Example format, x**2 - 5*sin(x) + x - 1): ", value="x**2 - 5*sin(x) + x - 1")
    tolerance = float(input("Tolerance: ")) if testing_mode == 1 else st.number_input("Tolerance: ", value=1e-6, format="%.1e")
    # - Class deployment protocols -
    deployment_protocols = Backend_deployment(a=a, b=b, tolerance=tolerance, iterations=iterations_cnt, equation=formula, deployment=web_deployment, testing_mode=testing_mode)
    extracted_function, derived_function, bijection_point, bij_iterations_used, bij_errors, x, nm_iterations_used, nm_errors = deployment_protocols.deploy()

    if testing_mode != 1:
        # - Deploy streamlit to display calculations on a page -
        st.write("### Root finding results")
        # - Display bisection methods results -
        st.write("**Bisection method**")
        st.write(f"Root: {bijection_point}")
        st.write(f"Iterations: {bij_iterations_used}")
        st.write(f"Tracked errors: {bij_errors}")
        # - Display newtons -
        st.write("**Newton's Method:**")
        st.write(f"Root: {x}")
        st.write(f"Iterations: {nm_iterations_used}")
        st.write(f"Tracked Errors: {nm_errors}")
        # - Display chart -
        fig, ax = plt.subplots()
        ax.plot(bij_errors, label="Bisection Method")
        ax.plot(nm_errors, label="Newton's Method", linestyle="dashed")
        ax.set_yscale("log")
        ax.set_xlabel("Iterations")
        ax.set_ylabel("Error (log scale)")
        ax.legend()
        st.pyplot(fig)