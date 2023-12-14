from random import randint

def get_random_password():
    
    result = ""
    count = 0
    while count < 8:
        random_symbol = chr(randint(40, 126))
        result += random_symbol
        count +=1
    return result

   