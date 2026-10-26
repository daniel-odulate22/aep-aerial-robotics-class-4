
import matplotlib.pyplot as plt

# Simulation settings
target_altitude = 10.0  # metres
altitude = 0.0           # starting altitude
velocity = 0.0
dt = 0.1                 # time step in seconds
simulation_time = 20

# PID gains (chosen for this simplified simulation)
Kp = 2.0
Ki = 0.1
Kd = 1.2

integral = 0.0
previous_error = 0.0

times = []
altitudes = []
errors = []

for step in range(int(simulation_time / dt)):
    time = step * dt

    # Calculate altitude error
    error = target_altitude - altitude

    # PID calculations
    integral += error * dt
    derivative = (error - previous_error) / dt

    control = (
        Kp * error
        + Ki * integral
        + Kd * derivative
    )

    # Simplified drone response model
    acceleration = control - 2.0 * velocity
    velocity += acceleration * dt
    altitude += velocity * dt

    # Keep the simulated altitude above ground
    if altitude < 0:
        altitude = 0
        velocity = 0

    # Save data for the graph
    times.append(time)
    altitudes.append(altitude)
    errors.append(error)

    previous_error = error

# Plot the results
plt.figure(figsize=(10, 5))
plt.plot(times, altitudes, label="Simulated altitude")
plt.axhline(
    y=target_altitude,
    linestyle="--",
    label="Target altitude (10 m)"
)
plt.xlabel("Time (seconds)")
plt.ylabel("Altitude (metres)")
plt.title("Drone Altitude Hold Using PID Control")
plt.grid(True)
plt.legend()
plt.show()

print(f"Target altitude: {target_altitude} m")
print(f"Final simulated altitude: {altitude:.2f} m")
