def make_set(data):
    if data is None:
        return []
    
    unique_list = []
    for num in data:
        if num not in unique_list:
            unique_list.append(num)
    
    return unique_list

def is_set(data):
    if data is None:
        return False

    return len(data) == len(make_set(data))

def union(setA, setB):
    if not is_set(setA) or not is_set(setB):
        return []

    return make_set(setA + setB)

def intersection(setA, setB):
    if not is_set(setA) or not is_set(setB):
        return []

    common = []
    for num in setA:
        if num in setB and num not in common:
            common.append(num)
    
    return common

setA_input = input("Enter at least 4 numbers for Set A, separated by commas: ")
setA = [int(x.strip()) for x in setA_input.split(",")]

if len(setA) < 4:
    print("Error: Set A must contain at least 4 numbers.")
else:
    print("Set A:", setA)
    print("your new setA:", make_set(setA))
    print("is it a set?:", is_set(setA))

    setB_input = input("Enter at least 4 numbers Set B (no repeats) separated by commas: ")
    setB = [int(x.strip()) for x in setB_input.split(",")]

    if len(setB) < 4:
        print("Error: Set B must contain at least 4 numbers.")
    else:
        print("Set B:", setB)
        print("Union of Set A and Set B:", union(make_set(setA), setB))
        print("Intersection of Set A and Set B:", intersection(make_set(setA), setB))
