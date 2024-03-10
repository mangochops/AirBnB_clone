def calculate_average(numbers):
    """
    Calculate the average of a list of numbers.

    Args:
        numbers (list of float): List of numbers.

    Returns:
        float: Average of the numbers.
    """
    if not numbers:
        return 0.0
    
    total = sum(numbers)
    average = total / len(numbers)
    return average

def main():
    numbers = [1.0, 2.5, 3.0, 4.5, 5.0]
    avg = calculate_average(numbers)
    print("Average:", avg)


if __name__ == "__main__":
    main()
