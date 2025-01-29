def parse_input(user_input):

    try:
        value, unit = user_input.split()
        return float(value), unit.lower()
    except ValueError:
        return None, None

def convert_measurement(value, unit):
    
    if unit == 'in':
        return round(value * 2.54, 2), 'cm'
    elif unit == 'cm':
        return round(value / 2.54, 2), 'in'
    elif unit == 'yd':
        return round(value * 0.9144, 2), 'm'
    elif unit == 'm':
        return round(value / 0.9144, 2), 'yd'
  
    elif unit == 'oz':
        return round(value * 28.349523125, 2), 'g'
    elif unit == 'g':
        return round(value / 28.349523125, 2), 'oz'
    elif unit == 'lb':
        return round(value * 0.45359237, 2), 'kg'
    elif unit == 'kg':
        return round(value / 0.45359237, 2), 'lb'
    else:
        return None, None

def main():
    
    user_input = input("Enter the value and unit (e.g., 10 in or 5 kg): ")
    value, unit = parse_input(user_input)
    
    if value is None or unit is None:
        print("Invalid input")
    else:
        converted_value, converted_unit = convert_measurement(value, unit)
        if converted_value is not None:
            print(f"{value} {unit} is equal to {converted_value} {converted_unit}.")
        else:
            print(f"conversion from {unit} is not supported.")

if __name__ == "__main__":
    main()