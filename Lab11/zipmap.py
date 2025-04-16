from itertools import zip_longest
from collections import Counter

def zipmap(key_list, value_list, override=False):
    pairs = list(zip_longest(key_list, value_list, fillvalue=None))

    if not override:
        key_counts = Counter(key_list)
        if any(count > 1 for count in key_counts.values()):
            return {}
        else:
            return dict(pairs)
    else:
        return dict(pairs)

if __name__ == "__main__":
    keys = input("Enter key list (comma-separated): ").split(",")
    values = input("Enter value list (comma-separated): ").split(",")
    override_input = input("Override duplicates? (y/n): ").lower() == "y"

    result = zipmap(keys, values, override_input)
    print("Resulting dictionary:", result)
