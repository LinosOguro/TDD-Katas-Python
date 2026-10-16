__author__ = 'smelnyk'

# http://codingdojo.org/cgi-bin/index.pl?KataRomanNumerals
# http://www.roman-numerals.org/chart100.html
# http://www.novaroma.org/via_romana/numbers.html
# http://www.roman-numerals.org/calculator.html


def get_roman_numeral(number):
    """
    Return the Roman Numeral represented by the number specified
    """
    # e.g. 5 -> "V", 1 -> "I"

    #print "Original number is: %s" % number

    numeral = ''

    if not isinstance(number, int):
        raise TypeError("The value you entered is invalid: {num} is not a positive integer.".format(num=number))

    if number <= 0:
        raise TypeError("The number you entered is invalid: {num} is not a positive integer.".format(num=number))

    while number >= 1000:
        numeral += 'M'
        number -= 1000

    if number >= 900 and number < 1000:
        numeral += 'CM'
        number -= 900

    while number >= 500:
        numeral += 'D'
        number -= 500

    if number >= 400 and number < 500:
        numeral += 'CD'
        number -= 400

    while number >= 100:
        numeral += 'C'
        number -= 100

    if number >= 90 and number < 100:
        numeral += 'XC'
        number -= 90

    while number >= 50:
        numeral += 'L'
        number -= 50

    if number >= 40 and number < 50:
        numeral += 'XL'
        number -= 40

    while number >= 10:
        numeral += 'X'
        number -= 10

    if number == 9:
        numeral += 'IX'
        number -= 9

    if number >= 5:
        numeral += 'V'
        number -= 5

    if number == 4:
        numeral += 'IV'
        number -= 4

    while number >= 1:
        numeral += 'I'
        number -= 1

    #print "Numeral String is: %s." % numeral
    return numeral


def get_number_from_roman_numeral(numeral):
    """
    Return the number represented by the single numeral
    """
    values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    numeral = numeral.upper()
    number = 0

    for index, roman_letter in enumerate(numeral):
        value = values[roman_letter]
        if index + 1 < len(numeral) and value < values[numeral[index + 1]]:
            number -= value
        else:
            number += value

    return number
