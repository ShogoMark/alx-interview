#!/usr/bin/python3
"""A method to determine if set of data is UTF8 encoding"""

def validUTF8(data):
    i = 0

    while i < len(data):
        num_bytes = 0

        # Get the number of bytes used for the current character
        leading_byte = data[i]

        # Determine the number of bytes used for the current character
        if leading_byte & 0x80 == 0: # Single byte character (starts with 0)
            num_bytes = 1
        elif leading_byte & 0xE0 == 0xC0:# Two-byte character (starts with 110)
            num_bytes = 2
        elif leading_byte & 0xF0 == 0xE0:# Three-byte character (starts with 1110)
            num_bytes = 3
        elif leading_byte & 0xF8 == 0xF0:# Four-byte character (starts with 11110)
            num_bytes = 4
        else:
            # Invalid leading byte, not a valid UTF-8 encoding
            return False

        # Check if there are enough bytes for the current character
        if i + num_bytes > len(data):
            return False

        # Check if the following bytes start with the pattern '10'
        for j in range(i + 1, i + num_bytes):
            if data[j] & 0xC0 != 0x80:
                return False

        # Move to the next character
        i += num_bytes

    # All bytes have been processed without any issues, so it's a valid UTF-8 encoding
    return True
