# Solve and plot impulsive differential equations for impulsive vaccination stategy

This repository was developed based on the publication 'Backward bifurcation for pulse vaccination', G. Rost and Zs. Vizi, 2014.

## Install
This project is developed and tested with Python 3.8+. To install project dependencies, execute the following steps:
1) Install *virtualenv*: `pip3 install virtualenv`
2) Create a virtual environment (named *venv*) in the project directory: `python3 -m venv venv`
3) Activate *venv*: `source venv/bin/activate`
4) Install dependencies from `requirements.txt`: `pip install -r requirements.txt`

## Simulation
Code for running the framework is available in folder `./src`. 
Here you find:
- the function which contains the model equations of the vaccination (`./src/functions.py`)
- the class for solving impulsive differential equations (`./src/solver.py`)
- the class for plotting the solution of the impulsive system (`./src/plotter.py`)
- the file which executes the simulation (`./src/main.py`)

## Plots
If you run the code, the plots will be generated in the in-use created folder `./plots`.