#!/usr/bin/env python3
# Function definitions.
def factor_sum(num): 
    """Prints the minimum A+B where A*B=num."""
    minsum = num + 1

    # Limit search to the square root of num.
    for i in range(1, (int(num**0.5) + 1)):
        if num % i == 0:
            candidate = (i + (num/i))
            # Update minsum if new A + B is smaller.
            if candidate < minsum:
                minsum = candidate
    return minsum

num_to_check = int(input("Enter number to find minimum sum of divisors: "))
print("A + B = {}".format(factor_sum(num_to_check)))
