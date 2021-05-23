import random

def lottery(size=10):
    randomlist = []
    stop = False

    while stop != True:
        number = random.randint(1,50)
        
        if number in randomlist :
            pass
        else :
            randomlist.append(number)
        
        if len(randomlist)==size:
            stop = True
    
    randomlist.sort()

    return randomlist


# try:
#     x = input("Enter the number of balls to lottery (default 10) : ")
#     y = lottery( int(x) )
#     print("The Lottery numbers are :")
#     print(y)
# except ValueError:
#     print("No valid integer! Please try again ...")