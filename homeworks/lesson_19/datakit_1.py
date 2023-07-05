# - Create an array with shape (4, 3) of: a. all zeros b. ones c. numbers from 0 to 11
# - Tabulate the following function: F(x)=2x^2+5, x∈[1,100] with step 1.
# - Tabulate the following function: F(x)=e^−x, x∈[−10,10] with step 1.

import numpy as np


# a = np.zeros((4, 3))

# b = np.ones((4, 3))

# c = np.arange(12).reshape((4,3))

# print(c)

# ________________________________


# x = np.arange(1, 101)

# F = 2 * x ** 2 + 5

# print(F)

#_______________________________

x = np.arange(-10, 11)

F = np.exp2(-x)

print(F)



