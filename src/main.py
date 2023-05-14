from src.solver import Solver
from src.functions import pulse_eq
from src.plotter import Plot
import os


p = {
    'I0': 1./2,
    'sigma': 0.1,
    'gamma': 0.89,
    'mu': 0.31,
    'theta': 0.01,
    'phi': 0.174,
    'T': 3,
    'beta': 2.22,
    'time': 30
}

sol = Solver(i0=p['I0'], v0=0, time=p['time'])

result = sol.solver_pulse(phi=p['phi'], model_equations=pulse_eq, vacc_time=p['T'],
                          params=(p['beta'], p['gamma'], p['mu'], p['theta'], p['sigma']))

os.makedirs("../plots", exist_ok=True)

# col = 0: susceptible, col = 1: infected, col = 2: vaccinated
p = Plot(results=result, vacc_time=p['T'], time=p['time'])
plot = p.plot_results(col=1)

