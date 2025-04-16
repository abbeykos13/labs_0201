from functools import reduce

def custom_filter(f, iterable):
    return reduce(
        lambda acc, item: acc + [item] if f(item) else acc,
        iterable,
        []
    )

if __name__ == "__main__":
    nums = input("Enter a list of numbers (comma-separated): ")
    nums = list(map(int, nums.split(",")))

    is_even = lambda x: x % 2 == 0
    result = custom_filter(is_even, nums)
    print("Filtered (even numbers):", result)
