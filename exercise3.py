integer_range = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
roman_range = ["M", "CM", "D", "CD","C", "XC", "L", "XL","X", "IX", "V", "IV","I"]

def integer_to_roman(number):
    roman = ""
    i = 0

    while number > 0:
        for _ in range(number // integer_range[i]):
            roman += roman_range[i]
            number -= integer_range[i]
        i += 1
    
    return roman

try:
    x = input("Enter your integer number:")
    y = integer_to_roman( int(x) )
    print (y)
except ValueError:
    print("No valid integer! Please try again ...")