import numpy as np
from scipy.integrate import odeint


class Solver:

    def __init__(self, i0: float, v0: float, time: int):
        self.v0 = 0
        self.i0 = i0
        self.s0 = 1 - i0 - v0
        self.time = time

    def solver_pulse(self, phi: float, vacc_time: int,
                     model_equations, params):
        """
        This function solves the model_equations of impulsive vaccination as an impulsive system.
        :param phi: parameter for the vaccination -> the ratio phi of the vaccinated don't get immunity
        :param vacc_time: the frequency of vaccination
        :param model_equations: function, which contain the model equations
        :param params: parameters of the model equations
        :return: 2D array of the solutions
                the ith row contains the S, I, V ratio of the ith time point
                the 0th row contains the initial S0, I0, V0
                the first column (index 0) corresponds to susceptible people
                the second column (index 1) corresponds to infected people
                the third column (index 2) corresponds to vaccinated people
            (time+time/vacc_time) rows
            3 columns
        """

        y0 = self.s0, self.i0, self.v0
        t = np.linspace(0, self.time, self.time)

        total = np.zeros((1, 3))

        for i in range(int(self.time/vacc_time)):
            result = odeint(model_equations, y0, t, args=params)
            s1 = (1-phi)*result[vacc_time, 0]
            i1 = result[vacc_time, 1]
            v1 = result[vacc_time, 2] + phi*result[vacc_time, 0]
            y0 = s1, i1, v1
            total = np.vstack((total, result[:vacc_time+1, :]))

        # the first row (index 0) is the initialization with zeros - we don't need it
        tot = total[1:, :]

        return tot
