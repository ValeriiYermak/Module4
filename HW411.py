# def is_valid_password(password):
    
#     len(value) == False
#     value_upper == False
#     value_lower == False
#     value_isdigit == False    
    
#     for value in password:
#         if value_upper == any(value.isupper()):         # верхній регістр
#             return        
#         if  value_lower == any(value.islower()):        # нижній регістр
#             return
#         if  value_isdigit == any(value.isdigit()):      # містить цифру
#             return
#         if len(value) != 0:                             # кількість символів - 0
#             return
#         if len(value) == 8:                             # кількість символів - 8
#             return

#     else:
#         return False
        

def is_valid_password(password):
    value_upper = False
    value_lower = False
    value_isdigit = False
    for value in password:
        if value.isupper():         # верхній регістр
            value_upper = True
        if  value.islower():        # нижній регістр
            value_lower = True
        if  value.isdigit():      # містить цифру
            value_isdigit = True
    if len(password) == 8 and value_isdigit and value_lower and value_upper:                             # кількість символів - 8
            return True
    else:
        return False






# def is_valid_password(password):
    
#     for value in password:
#         if value == any(value.isdigit() for value in password):
#             return 
#         if value == any(value.isupper() for value in password):
#             return
#         if value == any(value.islower() for value in password):
#             return
#         if len(password) == 0:
#             return False
#         if len(password) < 8:
#             return False
#     else:
#         return False
        



























# def is_valid_password(password):
  
#     if len(password) == 0:
#         return False
#     if len(password) < 8:
#         return False
#     if any(ch.isdigit() for ch in password):
#         if any(ch.isupper() for ch in password):
#             if any(ch.islower() for ch in password):
#                     print("Password is fine")
#                     return True
    