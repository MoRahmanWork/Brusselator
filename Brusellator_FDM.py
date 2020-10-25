"""Brusselator"""
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt

class Brusselator:
    """Brusselator"""
    def __init__(self, h=0.01, t_max=15, A=2, B=6, *args, **kwargs):
        self.A = A
        self.B = B
        self.h = h  # h increments
        self.t_max = t_max  # Set time-step and maximum time
        self.n_steps = round(self.t_max/self.h)  # This works out how long the arrays should be
        self.t = np.zeros(self.n_steps)  # time array
        self.x = np.zeros(self.n_steps)  # x array
        self.y = np.zeros(self.n_steps)  # y array
        self.start_time = dt.datetime.today()  # start time
        self.end_time = dt.datetime.today()  # end time
        self.run_time = self.end_time - self.start_time   # run time

    # Function F(t,x,y)
    @staticmethod
    def f_xy(x, y, A, B, *args, **kwargs):
        return A - (B * x) + (y * (x ** 2)) - x

    # Function G(t,x,y)
    @staticmethod
    def g_xy(x, y, A, B, *args, **kwargs):
        return (B * x) - ((x ** 2) * y)

    def rk4(self):
        # Iterate
        for i in range(1, self.n_steps):
            # use the RK4 algorithm
            m_1 = self.h * self.f_xy(self.x[i - 1], self.y[i - 1], self.A, self.B)
            n_1 = self.h * self.f_xy(self.x[i - 1], self.y[i - 1], self.A, self.B)

            m_2 = self.h * self.f_xy(self.x[i - 1] + 0.5 * m_1, self.y[i - 1] + 0.5 * n_1, self.A, self.B)
            n_2 = self.h * self.g_xy(self.x[i - 1] + 0.5 * m_1, self.y[i - 1] + 0.5 * n_1, self.A, self.B)

            m_3 = self.h * self.f_xy(self.x[i - 1] + 0.5 * m_2, self.y[i - 1] + 0.5 * n_2, self.A, self.B)
            n_3 = self.h * self.g_xy(self.x[i - 1] + 0.5 * m_2, self.y[i - 1] + 0.5 * n_2, self.A, self.B)

            m_4 = self.h * self.f_xy(self.x[i - 1] + m_3, self.y[i - 1] + n_3, self.A, self.B)
            n_4 = self.h * self.g_xy(self.x[i - 1] + m_3, self.y[i - 1] + n_3, self.A, self.B)

            self.x[i] = self.x[i - 1] + (m_1 + 2 * m_2 + 2 * m_3 + m_4) * (1 / 6)
            self.y[i] = self.y[i - 1] + (n_1 + 2 * n_2 + 2 * n_3 + n_4) * (1 / 6)
            self.t[i] = self.t[i - 1] + self.h
            # Update

        self.end_time = dt.datetime.today()
        self.run_time = self.end_time - self.start_time
        print(self.run_time)

    def graphs(self):
        # plot graph
        fig, ax = plt.subplots()
        ax.plot(self.x, self.y)
        ax.set(xlabel='x(t)', ylabel='y(t)', title='Phase plane (x,y)')
        ax.grid()
        fig.savefig("test.png")
        plt.show()
        # Plot a new graph
        # plotting both x(t) and y(t) to make it easy to compare
        # Create two subplots and unpack the output array immediately
        fig, (ax1, ax2) = plt.subplots(nrows=2, sharex=True)
        ax1.plot(self.t, self.x)
        ax1.set(xlabel='t', ylabel='x(t)', title='time dependent graph for x(t) and y(t)')
        ax2.plot(self.t, self.y)
        ax2.set(ylabel='y(t)')
        plt.show()

    def run_brusselator(self):
        self.rk4()
        self.graphs()

self = Brusselator(h=0.01, t_max=15, A=2, B=6)
self.run_brusselator()




# start_time = dt.datetime.today()
# h = 0.01
# tmax = 15
# nsteps = round(tmax/h)
# t = np.zeros(nsteps)
# x = np.zeros(nsteps)
# y = np.zeros(nsteps)
# # Set the initial condition in the first entry of the solution
# t[0] = 0  #  This is the first value of t
# x[0] = 0  # This is the first value of x
# y[0] = 1  # This is the first value of y
# A = 2  # Value of A
# B = 6  # Value of B
#
# #Function F(t,x,y)
# def F_xy(x, y, A, B, *args, **kwargs):
#     return A - (B * x) + (y * (x ** 2)) - x
#
# #Function G(t,x,y)
# def G_xy(x, y, A, B, *args, **kwargs):
#     return (B * x) - ((x ** 2) * y)
#
# # Iterate
# for i in range(1, nsteps):
#     # use the RK4 algorithm
#     m_1 = h * F_xy(x[i - 1] , y[i - 1], A, B)
#     n_1 = h * G_xy(x[i - 1] , y[i - 1], A, B)
#
#     m_2 = h * F_xy(x[i - 1] + 0.5 * m_1, y[i - 1] + 0.5 * n_1, A, B)
#     n_2 = h * G_xy(x[i - 1] + 0.5 * m_1, y[i - 1] + 0.5 * n_1, A, B)
#
#     m_3 = h * F_xy(x[i - 1] + 0.5 * m_2, y[i - 1] + 0.5 * n_2, A, B)
#     n_3 = h * G_xy(x[i - 1] + 0.5 * m_2, y[i - 1] + 0.5 * n_2, A, B)
#
#     m_4 = h * F_xy(x[i - 1] + m_3, y[i - 1] + n_3, A, B)
#     n_4 = h * G_xy(x[i - 1] + m_3, y[i - 1] + n_3, A, B)
#
#     x[i] = x[i-1] + (m_1 + 2 * m_2 + 2 * m_3 + m_4) * (1/6)
#     y[i] = y[i-1] + (n_1 + 2 * n_2 + 2 * n_3 + n_4) * (1/6)
#     t[i] = t[i-1] + h
#     # Update
# end_time = dt.datetime.today()
# run_time = end_time - start_time
# print(run_time)
# # plot graph
# fig, ax = plt.subplots()
# ax.plot(x, y)
# ax.set(xlabel='x(t)', ylabel='y(t)', title='Phase plane (x,y)')
# ax.grid()
# fig.savefig("test.png")
# plt.show()
# # Plot a new graph
# # plotting both x(t) and y(t) to make it easy to compare
# # Create two subplots and unpack the output array immediately
# f, (ax1, ax2) = plt.subplots(nrows=2, sharex=True)
# ax1.plot(t, x)
# ax1.set(xlabel='t', ylabel='x(t)', title='time dependent graph for x(t) and y(t)')
# ax2.plot(t, y)
# ax2.set(ylabel='y(t)')
# plt.show()
