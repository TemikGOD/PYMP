## First lab
## 19
import math

A = - math.pow(10, 3)
D = 10
rightResult = 2.96095E+1

result = round(math.sqrt((A * math.log(D)) / (2 - math.pi + math.log(D) * math.cos(math.log(D) - 31 * math.pow(10, -3)))), 4)
print(rightResult, result)
print(result == rightResult)

## 20
A = - math.pow(10, 4)
B = 0.2
C = -0.5
D = 3
rightResult = 5.26688E-1

result = round(math.sqrt(A * (3 * math.sin(D) - 9 * math.cos(abs(B)) + 10 * math.tan(C))) / (25 * math.pi * math.pow(D, 2)), 6)
print(rightResult, result)
print(result == rightResult)