# Intended to calculate the average of a list of numbers

def average(numbers)
    total = sum(numbers)
    avg = total / len(numbers)
    return avg

print(average([10, 20, 30, 40]))
