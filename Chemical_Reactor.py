import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
# from random import radiant

#Arrays of subtances A,B,C
A = []
B = []
C = []

#initial values of substances
int_A = 1  
int_B = .5
int_C = 0

k1, k2= .05, .05 #rate constant

A.append(int_A)
B.append(int_B)
C.append(int_C)

Time = 100
dt = .2

fig,ax = plt.subplots()
ax.set_xlim(0, (Time/dt)+5)
ax.set_ylim(0, 1.2)
Line_A, = ax.plot([], label = "A")
Line_B, = ax.plot([], label = "B")
Line_C, = ax.plot([], label = "C")

current_time = 0

def animate(i):
    global current_time, Time
    if current_time <= Time:
        A_next = A[-1] + (k2 * C[-1] - k1 * A[-1] * B[-1]) * dt
        B_next = B[-1] + (k2 * C[-1] - k1 * A[-1] * B[-1]) * dt
        C_next = C[-1] + (2 * k1 * A[-1] * B[-1] - 2 * k2 * C[-1]) * dt
        A.append(A_next)
        B.append(B_next)
        C.append(C_next)
        current_time += dt
    
    Line_A.set_data(range(len(A)),A)
    Line_B.set_data(range(len(B)),B)
    Line_C.set_data(range(len(C)),C)

animation = FuncAnimation(fig, animate, frames=700, interval = 1, repeat = False)

plt.legend()
plt.show()

print(len(A))
print(len(B))
