#!/usr/bin/python3
"""UTF-8 Validation"""


def validUTF8(data):
    """This function would check if a given data set represents a valid UTF-8
    encoding"""
    result = 0

    for num in data:
        """iterates through each element in the data list and
        performs AND operation between num and 0xff."""
        byte = num & 0xFF

        if result == 0:
            """
            checks if initial state, if the most bit is 0, it's a single-byte
            character. 3 bits are 110 it's the first 2-byte characters, if the
            first 5 bits are 11110, its the first byte of 4 bype character
            """
            if (byte >> 7) == 0:
                continue
            elif (byte >> 5) == 0b110:
                result = 1
            elif (byte >> 4) == 0b1110:
                result = 2
            elif (byte >> 3) == 0b11110:
                result = 3
            else:
                return False
        else:
            """if the first 2 bits are not 10 and its an invalid continuation
            byte. return False """
            if (byte >> 6) != 0b10:
                return False
            result -= 1
    return result == 0
