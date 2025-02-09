import streamlit as st
from Backend import Backend_deployment

# - Behavior mods -
developer_mode = 1
testing_mode = 1
web_deployment = 1

if web_deployment == 1:
    if testing_mode != 1:
        st.title("Root finding web app assignment")
    a = -4 if testing_mode == 1 else st.number_input("Interval start (a): ", value=-10.0)
    b = 9 if testing_mode == 1 else st.number_input("Interval start (b): ", value=10.0)
    formula = "(5*x+4)+1" if testing_mode == 1 else st.text_input("Enter function (e.g., x**2 - 5*sp.sin(x) + x - 1): ")
    tolerance = 0.5 if testing_mode == 1 else st.number_input("Tolerance: ", value=1e-6, format="%.1e")
    # - Class deployment protocols -
    deployment_protocols = Backend_deployment(a=a, b=b, tolerance=tolerance, iterations=500, equation=formula, deployment=web_deployment, testing_mode=testing_mode)
    deployment_protocols.deploy()