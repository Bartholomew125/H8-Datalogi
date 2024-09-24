import sys

numbers = {
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "A": 10,
    "B": 11,
    "C": 12,
    "D": 13,
    "E": 14,
    "F": 15,
}

to_number = {
    0: "0",
    1: "1",
    2: "2",
    3: "3",
    4: "4",
    5: "5",
    6: "6",
    7: "7",
    8: "8",
    9: "9",
    10: "A",
    11: "B",
    12: "C",
    13: "D",
    14: "E",
    15: "F",
}


def ConvertBaseToBase(n: str, fb: int, tb: int) -> str:
    """
    Converts a number n from a base fb to a new base tb
    and the returns a string with that number
    """

    # Flip for easier use :D
    n = n[::-1]

    # Converting number to base 10 via
    # a dictionary
    base_10_n = 0
    for i, char in enumerate(n):
        base_10_n += numbers[char] * fb**i
    base_10_n = int(base_10_n)

    # Creating the new number by integer division
    # and modulo for remainder
    new_number = ""
    while base_10_n > 0:
        kvotient = base_10_n // tb
        rest = base_10_n % tb
        new_number += str(to_number[rest])
        base_10_n = kvotient

    # reversing the number back
    new_number = new_number[::-1]

    return new_number


if __name__ == "__main__":
    # Get inputs
    number = sys.argv[1]
    from_base = int(sys.argv[2])
    to_base = int(sys.argv[3])

    # print converted number
    print(ConvertBaseToBase(number, from_base, to_base))
