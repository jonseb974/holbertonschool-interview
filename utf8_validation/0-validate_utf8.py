#!/usr/bin/python3
"""
Method that determines if a given data set represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """
    Return: True if data is a valid UTF-8 encoding, else return False
    """

    data_bytes = 0

    for data_byte in data:
        binary_str = format(data_byte, '08b')[-8:]

        if data_bytes == 0:
            if binary_str[0] == '0':  # Begining of new UTF-8 character
                continue  # single-bite character keep analysing the data.

            elif binary_str.startswith('110'):  # this is a two byte character
                data_bytes = 1

            elif binary_str.startswith('1110'):  # Three byte character.
                data_bytes = 2

            elif binary_str.startswith('11110'):  # Four byte character.
                data_bytes = 3
            else:
                return False  # Invalide sequence of byte.
        else:
            if binary_str.startswith('10'):  # Start in the middle of UTF-8
                data_bytes -= 1
            else:
                return False  # Invalid sequence of bytes
    return data_bytes == 0
