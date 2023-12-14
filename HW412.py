from random import randint


def get_random_password():
    result = ""
    count = 0
    while count < 8:
        random_symbol = chr(randint(40, 126))
        result = result + random_symbol
        count = count + 1
    return result


def is_valid_password(password):
    if len(password) != 8:
        return False

    has_upper = False
    has_lower = False
    has_num = False

    for ch in password:
        if ch.isupper():
            has_upper = True
        elif ch.islower():
            has_lower = True
        elif ch.isdigit():
            has_num = True

    return has_upper and has_lower and has_num


def get_password():
    
    shluz = True
    
    while shluz:
        pass_word = get_random_password()
        if is_valid_password(pass_word): 
            shluz = False 
    return pass_word



# def is_valid_password(password):
#     value_upper = False
#     value_lower = False
#     value_isdigit = False
#     for value in password:
#         if value.isupper():         # верхній регістр
#             value_upper = True
#         if  value.islower():        # нижній регістр
#             value_lower = True
#         if  value.isdigit():      # містить цифру
#             value_isdigit = True
#     if len(password) == 8 and value_isdigit and value_lower and value_upper:                             # кількість символів - 8
#             return True
#     else:
#         return False