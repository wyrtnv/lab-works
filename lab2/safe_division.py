def safe_divide(numerator, divisor):
    """
    Performs division of two numbers, handling ZeroDivisionError if the divisor is zero.
    """

    try:
        result = numerator / divisor  # denominator

    except ZeroDivisionError:
        error_message = "Error: Cannot divide by zero (ZeroDivisionError caught)."
        print(error_message)
        return None

    except TypeError:
        print("Error: Inputs must be numbers.")
        return None

    else:
        print(f"Success: {numerator} divided by {divisor} is {result}")
        return result


print("\n--- Test 1: Successful Division (50 / 5) ---")
safe_divide(50, 5)

print("\n--- Test 2: Division by Zero (10 / 0) ---")
safe_divide(10, 0)

print("\n--- Test 3: Division by a float zero (10 / 0.0) ---")
safe_divide(10, 0.0)

print("\n--- Test 4: Handling another type of error (10 / 'two') ---")
safe_divide(10, 'two')
