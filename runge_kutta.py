import numpy as np
import matplotlib.pyplot as plt


dt = 0.1
g = 9.8
cd = 0.4
area = 0.5
dry_mass = 400.0

#initial state
t = 0.0
mass = 1000

##state vector: [altitute,velocity]
y = np.array([0.0,0.0])

##telemetry logs
time_log = [t]
alt_log = [y[0]]
vel_log = [y[1]]

def get_derivatives(t_step,state,m):
    alt, vel = state

    #1.thrust/burn logic
    if t_step < 30:
        thrust = 15000   #stage 1
        burn_rate = 13.33
    elif 30 <= t_step < 50:
        thrust = 5000     #stage 2
        burn_rate = 10.0
    else:
        thrust = 0    #stage 3
        burn_rate = 0

    ##2. Atmospheric density logic
    if alt < 11000:
        rho = 1.225 * (1- 0.0000225 * alt)**4.25
    elif 11000 <= alt < 25000:
        rho = 0.364 * np.exp(-0.000157 * (alt - 11000))
    else:
        rho = 0

    ##3. Physics (net force = Thurst - weight - drag)
    drag = 0.5 * rho * (vel**2) * cd * area * np.sign(vel)
    weight = m * g
    accel = (thrust - weight - drag)/m

    return np.array([vel,accel]), burn_rate

#simulation loop
while y[0] >= 0:

    _,br = get_derivatives(t,y,mass)
    if mass > dry_mass:
        mass -= br * dt

    #RK4
    k1, _ = get_derivatives(t, y, mass)
    k2, _ = get_derivatives(t + dt/2, y + (dt/2) * k1, mass)
    k3, _ = get_derivatives(t + dt/2, y + (dt/2) * k2, mass)
    k4, _ = get_derivatives(t + dt, y + dt*k3, mass)

    y = y + (dt/6.0) * (k1 + 2*k2 + 2*k3 + k4)
    t+= dt

    #store telemetry

    time_log.append(t)
    alt_log.append(y[0])
    vel_log.append(y[1])

    if t > 1000:
        break

##b. calculate maximums
max_alt = max(alt_log)
max_vel = max(vel_log)

print(f"Maximum Altitude: {max_alt:.2f} m")
print(f"Maximum Velocity: {max_vel:.2f} m/s")


### c. generate plots_file
plt.figure(figsize=(12,5))

#time vs Altitude
plt.subplot(1,2,1)
plt.plot(time_log, alt_log, color = "blue", linewidth = 2)
plt.title("Time vs Altitude (RK4)")
plt.xlabel("Time(s)")
plt.ylabel("height (m/s)")
plt.grid(True, alpha = 0.3)

##time vs velocity
plt.subplot(1,2,2)
plt.plot(time_log, vel_log, color = "green", linewidth = 2)
plt.title("Time vs Velocity (RK4)")
plt.xlabel("Time(s)")
plt.ylabel("Speed(m/s)")
plt.grid(True, alpha = 0.3)

plt.tight_layout()
plt.savefig("rocket_RK4_analysis.png", dpi = 300, bbox_inches = "tight")
plt.show()
