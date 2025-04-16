def group_by(f, target_list):
    result = {}
    for item in target_list:
        key = f(item)
        if key not in result:
            result[key] = []
        result[key].append(item)
    return result

if __name__ == "__main__":
    items_input = input("Enter list of strings (comma-separated): ")
    target_list = [item.strip() for item in items_input.split(',') if item.strip()]

    result = group_by(len, target_list)
    print("Result:", result)