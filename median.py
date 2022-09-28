"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

def median(numList):
    n = len(numList)
    sortedList = numList.copy()
    sortedList.sort()
    mid= (n-1)//2
    if (n%2):
        return (sortedList[mid])
    else:
        return (sortedList[mid] + sortedList[mid+1])/2


while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
print(numbers)
print(median(numbers))
