## lab 3
## 19

import random

numOfNums = 0;
bordersOfNums = [-1000, 1000]

while (True):
    print("Enter the number of numbers(not less than 100): ")
    numOfNums = int(input())
    if (numOfNums < 100):
        print("number must be not less than 100, try again")
    else:
        break

nums = [random.uniform(bordersOfNums[0], bordersOfNums[1])]
count = 1
while (count < numOfNums):
    num = random.uniform(bordersOfNums[0], bordersOfNums[1])
    same = False
    for item in nums:
        if (item == num):
            same = True
            break
    if (same == False):
        nums.append(num)
        count += 1

exitCount = 0
count = 0
resultNums = []

while (exitCount < 3):
    for item in nums:
        if (item < 0):
            exitCount += 1
            if (exitCount == 3):
                break
        count += 1
        resultNums.append(item)
        print(item)

result = 0
for item in resultNums:
    result += item
result = result / count

print("result: ", result)

## 20

numOfNums = 0;
bordersOfNums = [-1000, 1000]

while (True):
    print("Enter the number of numbers(not less than 100): ")
    numOfNums = int(input())
    if (numOfNums < 100):
        print("number must be not less than 100, try again")
    else:
        break

nums = [random.randint(bordersOfNums[0], bordersOfNums[1])]
count = 1
while (count < numOfNums):
    num = random.randint(bordersOfNums[0], bordersOfNums[1])
    same = False
    for item in nums:
        if (item == num):
            same = True
            break
    if (same == False):
        nums.append(num)
        count += 1

min = 100000
for item in nums:
    if (item < min):
        min = item

result = min
if (result < 0):
    print("Result:", result)
else:
    print("There is no result")