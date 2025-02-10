import logging, datetime
import numpy as np
import math
import streamlit as st
from Functionalities import parser, bisection_protocols, newtons_method

class Backend_deployment():
    def __init__(self, a: [float, int], b: [float, int], tolerance: float, iterations: int, equation: str, deployment: int, testing_mode: int):
        self.a = a
        self.b = b
        self.tolerance = tolerance
        self.iterations = iterations
        self.equation = equation
        self.deployment_clearance = deployment
        self.testing_mode = testing_mode
    def deploy(self):
        if self.deployment_clearance != 1:
            logging.info("Deployment bricked. Manually reactivate.")
            quit("Deployment bricked. Manually reactivate.")

        extracted_function, derived_function = parser(self.equation, testing_mode=self.testing_mode)
        # -> Bijection <-
        bijection_point, bij_iterations_used, bij_errors = bisection_protocols(extracted_function, self.a, self.b, tolerance=self.tolerance)
        # -> Newtons method <-
        x, nm_iterations_used, nm_errors = newtons_method(f=extracted_function,df=derived_function,x_0=self.a, tolerance=self.tolerance, max_iterations=self.iterations)

        if  self.testing_mode == 1:
            # - Streamlit disabled -
            testing_mode_start = datetime.datetime.now()
            print("--------------------")
            print(" - Bijection protocols results - ")
            print(f"Bijection point: {bijection_point}\nInteration: {bij_iterations_used}\nErrors: {bij_errors}")
            print("--------------------")
            print(" - Newtons method - ")
            print(f"Iterations: {nm_iterations_used}\nErrors tracked: {nm_errors}")
            print("--------------------")
            testing_mode_end = datetime.datetime.now() - testing_mode_start
            print(f"Processing time: {testing_mode_end}")

        return extracted_function, derived_function, bijection_point, bij_iterations_used, bij_errors, x, nm_iterations_used, nm_errors