import logging

import numpy as np
import math

class Backend_deployment():
    def __init__(self, a: [float, int], b: [float, int], tolerance: float, iterations: int, equation: str, deployment: int):
        self.a = a
        self.b = b
        self.tolerance = tolerance
        self.iterations = iterations
        self.equation = equation
        self.deployment_clearance = deployment
    def deploy(self):
        if self.deployment_clearance != 1:
            logging.info("Deployment bricked. Manually reactivate.")
            quit("Deployment bricked. Manually reactivate.")
