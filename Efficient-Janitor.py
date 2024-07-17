def efficientJanitor(weight):
    weight.sort()  # Sort the weights
    i = 0  # Pointer for the lightest bag
    j = len(weight) - 1  # Pointer for the heaviest bag
    trips = 0

    while i <= j:
        if weight[i] + weight[j] <= 3.00:
            # Can carry both bags
            i += 1  # Move to the next lightest bag
        # Carry the heaviest bag (either paired or alone)
        j -= 1
        trips += 1  # Count this trip

    return trips

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    n = int(data[0])  # First line is the number of bags
    weight = [float(data[i + 1]) for i in range(n)]  # Next lines are the weights

    result = efficientJanitor(weight)
    print(result)  # Print the result
