import time

def calculate_stats(numbers):
    print("DEBUG: entering calculate_stats")
    print(f"DEBUG: input = {numbers}")
    
    total = 0
    for i in range(len(numbers)):
        total = total + numbers[i]
    
    avg = total / len(numbers)
    
    # unoptimized: recalculates max/min with nested loops instead of using max()/min()
    maximum = numbers[0]
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if numbers[i] > maximum:
                maximum = numbers[i]
    
    minimum = numbers[0]
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if numbers[i] < minimum:
                minimum = numbers[i]
    
    print(f"DEBUG: total={total}, avg={avg}, max={maximum}, min={minimum}")
    return {"total": total, "average": avg, "max": maximum, "min": minimum}


def find_duplicates(items):
    print("DEBUG: checking for duplicates")
    duplicates = []
    
    # unoptimized: O(n^2) comparison instead of using a set
    for i in range(len(items)):
        for j in range(len(items)):
            if i != j and items[i] == items[j]:
                if items[i] not in duplicates:
                    duplicates.append(items[i])
    
    time.sleep(0.1)  # leftover debug delay, not needed
    print(f"DEBUG: found duplicates = {duplicates}")
    return duplicates


if __name__ == "__main__":
    data = [4, 2, 7, 2, 9, 4, 1]
    print(calculate_stats(data))
    print(find_duplicates(data))