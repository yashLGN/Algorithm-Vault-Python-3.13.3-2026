'''

The Luhn algorithm, also known as the "modulus 10" or "mod 10" algorithm, 
is a simple checksum formula used to validate a variety of identification numbers, 
like credit card numbers. These are the steps to validate a number using 
the Luhn algorithm:

Starting from the right, and excluding the rightmost digit (the check digit), 
double the value of every other digit.

If the result of doubling a digit is greater than 9, sum the digits to get 
a single digit. Alternatively, you can subtract 9 from the result.

Take the sum of all the digits including the check digit.

If the sum of all the digits is a multiple of 10, then the number is valid; 
else it is not valid.

'''

def verify_card_number(card_number):
    # Remove spaces and dashes
    card_number = card_number.replace(' ', '').replace('-', '')

    # Convert to list of integers
    digits = [int(num) for num in card_number]

    check_digit = digits.pop()  # last digit removed

    digits.reverse()

    for i in range(len(digits)):
        if i % 2 == 0: 
            digits[i] *= 2
            if digits[i] > 9:
                digits[i] -= 9

    total = sum(digits) + check_digit

    # Return the validity
    return 'VALID!' if total % 10 == 0 else 'INVALID!'