import numpy as np
import math

class Backend_deployment():
    def __init__(self, a: [float, int], b: [float, int], tolerance: float, iterations: int, equation: str):
        self.a = a
        self.b = b
        self.tolerance = tolerance
        self.iterations = iterations
        self.equation = equation
    def deploy(self):
        pass