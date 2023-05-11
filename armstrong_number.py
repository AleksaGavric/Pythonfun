def find_armstrong_numbers():
    """
    Finds Armstrong numbers in the range of 0 to 999, brute forcé :)
    An Armstrong number is a number that is equal to the sum of its own digits each raised to the power of the number of digits.
    """
    count = 0  # Count the number of Armstrong numbers found

    for thousands in range(10):
        e = 10000 * thousands
        for hundreds in range(10):
            d = 1000 * hundreds
            for tens in range(10):
                a = 100 * tens
                for units in range(10):
                    b = 10 * units
                    for z in range(10):
                        c = z

                        aps = (
                            a + b + c + d + e
                        )  # Calculate the sum of individual digits
                        n = 3  # Set the power value for Armstrong calculation
                        bes = (
                            (tens**n)
                            + (units**n)
                            + (z**n)
                            + (hundreds**n)
                            + (thousands**n)
                        )  # Calculate the Armstrong number

                        if bes == aps and aps != 0 and aps != 1:
                            print("Armstrong number:", bes)
                            count += 1

    print(count, "Armstrong numbers found under 1000!")


if __name__ == "__main__":
    find_armstrong_numbers()
