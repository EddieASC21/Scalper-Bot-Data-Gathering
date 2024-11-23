# Scalper-Bot-Data-Gathering

![Scalper Bot Data Gathering Poster](Scalper-Bot-Data-Gathering.png)

## Overview
This project simulates a queue system designed to process different types of customers—humans, autofill users, and bots. Each customer type has unique properties like arrival time, service time, and the resources they consume from the queue. This simulation helps visualize how different strategies can impact the efficiency and fairness of queue management, especially in systems susceptible to scalping bots.

## Project Structure
The simulation categorizes customers into three types:
- **Human:** Regular users who follow standard queue procedures.
- **Autofill:** Users who utilize autofill capabilities, potentially speeding up their processing time.
- **Bots:** Automated systems that attempt to monopolize queue resources faster than typical users.

## Features
- Simulate various customer interactions with a queue system.
- Analyze the impact of different customer types on resource allocation.
- Implement defense mechanisms like CAPTCHA and proxy detection to manage bot activity.

## How It Works
The simulation runs in several steps:
1. **Customer Generation:** Customers are generated with specific attributes such as arrival and service times.
2. **Queue Management:** The system processes customers based on the available resources and their arrival and service times.
3. **Defense Simulation:** Different strategies (e.g., CAPTCHA, Proxy restrictions) are tested against bots to evaluate their effectiveness.

### Classes and Methods
- `Customer`: Defines the properties of a customer in the queue.
- `Queue`: Manages the operations of the queue, including customer service and resource allocation.
- `simulateQueue`: Runs the simulation without any defenses.
- `simulateQueue_CA`: Simulates the queue with CAPTCHA as a defense mechanism.
- `simulateQueue_PR`: Uses Proxy restrictions to manage bot access.

## Usage
To run the simulation:
1. Ensure Python and necessary libraries (`numpy`, `seaborn`, `matplotlib`) are installed.
2. Execute the script to see how different customers interact with the queue.
3. Analyze the output graphs to understand the distribution of resources and effectiveness of bot management strategies.

## Installation
```bash
pip install numpy seaborn matplotlib
```

## Running Tests
To perform a simulation, you can call the specific test functions:
- `test1_simulation()`: Runs the basic queue simulation.
- `test2_simulation()`: Applies CAPTCHA defenses.
- `test3_simulation()`: Implements Proxy defenses.

## Visualization
The project utilizes **Seaborn** and **Matplotlib** to visualize the results of the simulations. This includes pie charts and bar graphs that show how resources are distributed among different customer types and how effectively the defenses work against bots.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.