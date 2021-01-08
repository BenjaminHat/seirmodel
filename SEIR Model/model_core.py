import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from scipy.integrate import odeint

# S => stock of susceptible population
# E => stock of exposed population
# I => stock of infected population
# R => stock of removed population
# N ==> total pop ===> N = S+I+R
# beta => number of person infected by one person per day
# D => duration of infections in days
# 1/delta ==> incubations period in days


class Model: ## SIR model
    def __init__(self, pop, agent_0, beta, D, delta,time):
        self.pop=pop
        self.agent_0=agent_0
        self.beta=beta
        self.gamma=1/D
        self.delta=1/delta
        self.time=np.linspace(0,time,time)
        self.vector = self.pop, self.agent_0, 0, 0

    def run_model(self):
        ret = odeint(self.__run_model_backward, self.vector,self.time)
        S, E, I, R = ret.T
        return S, E, I, R


    def __run_model_backward(self,vector,t):
        S, E, I, R = vector
        dSdt = - self.beta * S * I / self.pop
        dEdt = self.beta * S * I / self.pop - self.delta * E
        dIdt = self.delta * E - self.gamma * I
        dRdt = self.gamma * I
        return dSdt,dEdt,dIdt,dRdt

    def plot(self,vector):
        t = self.time
        S, E, I, R = vector
        fig = Figure(figsize=(6,6))
        ax = fig.add_subplot(111, facecolor='#dddddd', axisbelow=True)
        ax.plot(t, S / self.pop, 'b', alpha=0.5, lw=2, label='Susceptible')
        ax.plot(t,E / self.pop, 'y', alpha=0.5, lw=2, label='Exposed' )
        ax.plot(t, I / self.pop, 'r', alpha=0.5, lw=2, label='Infected')
        ax.plot(t, R / self.pop, 'g', alpha=0.5, lw=2, label='Recovered with immunity')
        ax.set_xlabel('Time /days')
        ax.set_ylabel('Number (1000s)')
        ax.set_ylim(0, 1.2)
        ax.yaxis.set_tick_params(length=0)
        ax.xaxis.set_tick_params(length=0)
        ax.grid(b=True, which='major', c='w', lw=2, ls='-')
        legend = ax.legend()
        legend.get_frame().set_alpha(0.5)
        for spine in ('top', 'right', 'bottom', 'left'):
            ax.spines[spine].set_visible(False)
        return fig

if __name__=="__main__":

    cov=Model(999, 1, 1, 4, 3, 100)
    print(cov.vector)
    cov.plot(cov.run_model())

