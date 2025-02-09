import streamlit as st
from Backend import Backend_deployment

# - Behavior mods -
developer_mode = 1
web_deployment = 0

if web_deployment == 1:
    st.title("Root finding web app assignment")
    a = 0
    b = 0
    formula = "(5x+4)+1"
    tolerance = 0.5
    Backend_deployment(a=a, b=b, tolerance=tolerance, iterations=500, equation=formula, deployment=web_deployment)
