
## LabWork 2
## 19

import math as m

A0 = 1.5
B0 = 2
A1 = -1.5
B1 = -2
A2 = 0
B2 = -5.8
vars = [[A0, B0], [A1, B1], [A2, B2]]
rightResults = [3.1602, -2.3872, -0.4959]

def calcResult(A, B) :
    if (A + B > 0): 
        return 2.8765 * m.log(A * B) 
    else:
        if (A + B <= 0 and B > -2.8765):
            return m.cos(2.8765 * A) + B
        else:
            return 2.8765 / B

for i in range(3):
    print("result of calculation:", calcResult(vars[i][0], vars[i][1]))
    print("right result :", rightResults[i])

## 20

A0 = 1
B0 = 1.0
A1 = -1
B1 = 2
A2 = 0.5
B2 = 2
vars = [[A0, B0], [A1, B1], [A2, B2]]
rightResults = [4.1212, -0.2264, 3.8982]

def calcResult(A, B) :
    if (A > 0.777 and B > 0.777): 
        return m.pow(A, 3.1212) + 3.1212 * m.pow(B, 0.777) 
    else:
        if (A < -0.777 or B < -0.777):
            return 0.777/3.1212 * m.sin(A * B)
        else:
            return 0.777 + A * B * 3.1212

for i in range(3):
    print("result of calculation:", calcResult(vars[i][0], vars[i][1]))
    print("right result :", rightResults[i])