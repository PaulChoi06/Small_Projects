import random

def estimate(num_points):
    in_circle = 0
    out_circle = 0

    for i in range(num_points):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)

        if x**2 + y**2 <= 1:
            in_circle += 1
        
        out_circle += 1

    return 4 * in_circle / out_circle

num = int(input())

print("pi estimate (using " + str(num) + " points): " + str(estimate(num)))

