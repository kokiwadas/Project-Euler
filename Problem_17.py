# If the numbers 1 to 5 are written out in words:
# one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters
# and 115 (one hundred and fifteen) contains 20 letters.
# The use of "and" when writing out numbers is in compliance with British usage.


def conversion(number):

    number = int(number)
    print('Number: ' + str(number))
    num_to_let = {1: ("one", "eleven"),
                  2: ("two", "twelve", "twenty"),
                  3: ("three", "thirteen", "thirty"),
                  4: ("four", "fourteen", "forty"),
                  5: ("five", "fifteen", "fifty"),
                  6: ("six", "sixteen", "sixty"),
                  7: ("seven", "seventeen", "seventy"),
                  8: ("eight", "eighteen", 'eighty'),
                  9: ("nine", "nineteen", "ninety"),
                  0: ("zero", "ten", "hundred", 'thousand')}

    converted = ''
    num_str = str(number)
    length = len(num_str)
    print('Length: ' + str(length))

    if length == 4:
        converted += num_to_let[int(num_str[0])][0] + ' '
        converted += num_to_let[0][3] + ' '
        length -= 1


    return converted

print(conversion(3000))


