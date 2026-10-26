# Drone Altitude Control Using PID

## Overview

This project demonstrates a Proportional-Integral-Derivative (PID) control loop using a simple Python simulation. The aim is to simulate how a drone can adjust its altitude to reach and maintain a target height.

The simulation uses a target altitude of 10 metres and observes how the simulated altitude changes over 20 seconds.

## Objectives

- Understand the basic concept of PID control.
- Simulate a feedback control loop for drone altitude.
- Observe how the controller responds to altitude error.
- Visualise the simulated altitude against the target altitude.

## What Is PID Control?

PID stands for Proportional, Integral, and Derivative. It is a feedback control method used to reduce the difference between a desired value and a measured value.

The controller has three components:

- **Proportional (P):** Produces a correction based on the current error.
- **Integral (I):** Accounts for accumulated error over time.
- **Derivative (D):** Responds to how quickly the error changes.

These components work together to calculate a control response.

## How the Simulation Works

The simulation follows these steps:

1. Set the target altitude to 10 metres.
2. Initialise the simulated altitude and velocity.
3. Calculate the difference between the target and current altitude.
4. Calculate the proportional, integral, and derivative terms.
5. Combine the three terms to calculate the control response.
6. Update the simulated velocity and altitude.
7. Repeat the process over 20 seconds.
8. Plot the simulated altitude against the target altitude.

The simulation uses Python and Matplotlib to perform the calculations and display the results.

## Results and Observations

The graph shows the simulated altitude as a solid line and the target altitude as a dashed line.

The simulated altitude rises towards the target of 10 metres. It briefly overshoots the target before gradually moving closer to it.

At the end of the 20-second simulation, the output reports a final simulated altitude of approximately **10.21 metres**.

This means the final altitude is approximately 0.21 metres above the target. The result demonstrates how a feedback controller can bring a simulated system close to a desired value.

## Limitations

This project uses a simplified mathematical model for learning purposes. It does not represent every physical force or behaviour of a real drone.

The simulation does not include a detailed quadcopter model, real sensor measurements, wind disturbances, or actual motor dynamics. Its results should therefore not be treated as proof that the controller is ready for use on a physical drone.

## Conclusion

This project demonstrates the basic operation of a PID feedback control loop through a simulated drone altitude-control problem.

By repeatedly calculating altitude error and adjusting the control response, the simulation brings the altitude close to its target. The graph also illustrates that a controller may overshoot the target before settling closer to it.

## Tools Used

- Python
- Matplotlib
- Google Colab

## Project Files

- `pid_altitude_control.py` - Python simulation code used in google colab
- `README.md` - Project explanation and results.
- `pid-altitude-plot.png` - Simulation graph.
