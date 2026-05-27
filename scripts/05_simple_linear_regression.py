"""
Simple linear regression
"""
import numpy as np
import matplotlib.pyplot as plt

# Testdata generation
# Features

X = np.array([i for i in range(5)])

# Target values
y = np.array([2,4,5,4,5])

# plt.figure(figsize=(8,5))
# plt.scatter(x=X,y=y)
# plt.show()
print(f"X:    {X}")
print(f"y:    {y}")

# Define the hypothesis
theta0 = 0
theta1 = 0

y_pred = theta0 + theta1 * X
print(f"Pred: {y_pred}")

# Errors:
errors = y_pred - y
print(f"Erro: {errors}")

# Cost function
m = len(X)
cost = (1/(2*m)) * np.sum(errors**2)   # 1/2m  for derivation of the cost function later-on

print(f"Cost: {cost}")
