import string
import os
import sys


global CHAR_LOOKUP 
CHAR_LOOKUP = list(string.digits + string.ascii_uppercase) 


"""
Hello, the code is editable, so make it your own :)
The main function is convert(), the rest of the code is optional.

If you like my program, let me know in my github page <3
-> https://github.com/ZKAW/base-to-base-converter
 
If you have any issue, please open a ticket in my github page.
-> https://github.com/ZKAW/base-to-base-converter/issues/new/choose
"""

def exit_msg(): # just some credits
    print("Thank you for using my base converter !\n")
    print("If you liked it, you can star me in github <3")
    print("https://github.com/ZKAW/base-to-base-converter")
    quit()
exit = exit_msg


def convert(number, frombase, tobase): # function to convert any base in any base
    """
    How to use:
    convert(<number or character to convert>, <input base ex: 10>, <output base ex:2>)
    => Exemple: convert(12,10,2) -> Output: 1100.
    => Exemple: convert(A,16,10) -> Output: 10.
    """

    global CHAR_LOOKUP 

    fromdigits = CHAR_LOOKUP[:int(frombase)]
    todigits = CHAR_LOOKUP[:int(tobase)] 
    

    if str(number)[0] == '-': 
        number = str(number)[1:] 
        neg = 1 
        
    else:
        neg = 0 

    # make a string of the integer (ex: A=10)
    x = 0
    for digit in str(number): 
        try:
            x = x * len(fromdigits) + fromdigits.index(digit)
        except ValueError:
            os.system('cls')
            print(f"\"{digit}\" is not in the selected input base")
            select()
             
    # créer le résultat dans la base 'len(todigits)'
    if x < 1:
        res = todigits[0]
    else:
        res = ""
        while x > 0:
            digit = x % len(todigits)
            res = todigits[digit] + res

            x = int(x / len(todigits))
        if neg:
            res = '-' + res
    return res

os.system('cls')

def select(): # function to get an entry from the user

    """
    This function is modulable, and optional.
    We could just do print(convert(n,b1,b2)) 
    """

    global number
    global frombase
    global tobase
    
    try: # Used to see if the user wants to convert a base directly from the command line arguments
        if "--help" in sys.argv[1]:    
            print("Format: python3",__file__,"<number or letter> <input base> <output base>")
            exit()
        if sys.argv[1] and sys.argv[2] and sys.argv[3] != "":
            try:
                number = sys.argv[1] 
                number = number.upper() 
                frombase = int(sys.argv[2]) 
                tobase = int(sys.argv[3]) 
                return          

            except ValueError: 
                os.system('cls') 
                print("Enter only enter numbers in [0-9]") 
                exit() 
    except IndexError:
        pass

    try:
        # define variables for the function select()
        number = input('Enter a number or a letter: ') 
        number = number.upper() 
        frombase = int(input("What's the input base? (>1): ")) 
        tobase = int(input("What's the output base? (>1): ")) 
    except ValueError: 
        os.system('cls') 
        print("Enter only enter numbers in [0-9]") 
        select() 

try:
    select() 
except KeyboardInterrupt: 
    os.system('cls')
    exit()

os.system('cls')

print(f"Original number in base{frombase}: {number}") 
print(f"Converted number in base{tobase}:",convert(number=number, frombase=frombase, tobase=tobase),"\n")

exit()