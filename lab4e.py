#!/usr/bin/env python3
# Author ID: [seneca_id]

def is_digits(sobj):
    # Check if all characters in the string are digits
    for char in sobj:
        if not char.isdigit():  # If any character is not a digit
            return False
    return True  # All characters are digits

if __name__ == '__main__':
    test_list = ['x3058', '3058', '8503x', '8503']
    for item in test_list:
        if is_digits(item):
            print(item, 'is an integer.')
        else:
            print(item, 'is not an integer.')
