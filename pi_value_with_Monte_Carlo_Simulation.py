import random
import numpy as np

def throw_needles(needle_num):
    in_circle = 0
    for n in range(1, needle_num+1):
        x = random.random() 
        y = random.random()
        if (x**2 + y**2) ** 0.5 <= 1.0:
            in_circle+=1
    return 4*(in_circle / float(needle_num))

def get_estimation(num_needle, num_trials):
    estimates = []
    for i in range(num_trials):
        pi_guess = throw_needles(num_needle)
        estimates.append(pi_guess)
    std_dev = np.std(estimates)
    estimation = sum(estimates) / len(estimates)
    print(f"est = {estimation}, std_dev = {std_dev} \
          needles: {num_needle}")
    return (estimation, std_dev)

def pi_estimation(precision, num_trials):
    needle_num = 1000
    std_dev = precision
    while precision <= 2*std_dev:
        estimation, std_dev = get_estimation(needle_num, num_trials)
        needle_num *= 2
    return estimation

random.seed(0)
pi_estimation(0.005, 100)

