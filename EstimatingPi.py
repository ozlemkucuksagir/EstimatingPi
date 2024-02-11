import numpy as np
import matplotlib.pyplot as plt

# Monte Carlo Method to PiEstimation
def estimate_pi_mc(N, distribution):
    

    # Generate random points based on the specified distribution
    if distribution == "Uniform":
        points = []
        while len(points) < N:
            x, y = np.random.uniform(),np.random.uniform()            
            points.append((x, y))
        points = np.array(points)
    elif distribution == "Normal":
        points = []
        while len(points) < N:
            x, y = np.random.normal(0.5, 0.5, 2)
            if x <= 1 and y <= 1 and x >= 0 and y >= 0:
                points.append((x, y))
        points = np.array(points)

    elif distribution == "Chisquare":
        points = []
        while len(points) < N:
            x = np.random.chisquare(2)
            y = np.random.chisquare(2)
            if x <= 1 and y <= 1 and x >= 0 and y >= 0:
                points.append((x, y))
        points = np.array(points)


    elif distribution == "Poisson":
        points = []
        while len(points) < N:
            x = np.random.poisson(0.5)
            y = np.random.poisson(0.5)
            if x <= 1 and y <= 1 and x >= 0 and y >= 0:
                points.append((x, y))
        points = np.array(points)


    elif distribution == "Power":
        points = []
        while len(points) < N:
            x = np.random.power(2)
            y = np.random.power(2)
            if x <= 1 and y <= 1 and x >= 0 and y >= 0:
                points.append((x, y))
        points = np.array(points)


    elif distribution == "Rayleigh":
        points = []
        while len(points) < N:
            x = np.random.rayleigh(0.5)
            y = np.random.rayleigh(0.5)
            if x <= 1 and y <= 1 and x >= 0 and y >= 0:
                points.append((x, y))
        points = np.array(points)


    else:
        raise ValueError("Invalid distribution type")

    inside_circle = np.sum(np.linalg.norm(points, axis=1) <= 1)
    pi_estimate = 4 * inside_circle / N
    return pi_estimate, points

distributions = ["Uniform", "Normal", "Chisquare", "Poisson", "Power", "Rayleigh"]
pi_estimates = []

# Perform Pi estimation for each distribution
for distribution in distributions:
    pi_estimate, _ = estimate_pi_mc(1000000, distribution)
    pi_estimates.append(pi_estimate)
    print(f"Pi Estimate for {distribution} Distribution: {pi_estimate}")


# Plotting Histograms
plt.figure(figsize=(15, 10))
for i, distribution in enumerate(distributions, 1):
    pi_estimate, points = estimate_pi_mc(1000000, distribution)
    plt.subplot(2, 3, i)
    if distribution=='Poisson':
        plt.hist(points[:, 0], bins=1000, color='mediumvioletred', label=f'{distribution.capitalize()} Distribution',linewidth=6)
    else: 
        plt.hist(points[:, 0], bins=1000, color='mediumvioletred', label=f'{distribution.capitalize()} Distribution')
        plt.title(f'{distribution} Distribution')
        plt.xlabel("X Values")
        plt.ylabel("Frequency")
        plt.legend()
plt.show()


plt.figure(figsize=(10, 5))
plt.bar(distributions, pi_estimates, color='mediumvioletred')
plt.title("Pi Estimates for Different Distributions")
plt.xlabel("Distribution")
plt.ylabel("Pi Estimate")
plt.show()