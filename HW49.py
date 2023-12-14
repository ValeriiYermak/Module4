pin_codes = ["1101", "9034", "0011"]

def is_valid_pin_codes(pin_codes):

    if len(pin_codes) < 1:
        return False
    
    if len(pin_codes) != len(set(pin_codes)):
        return False
    
    for pin in pin_codes:
        if len(pin) != 4:
            return False
        if not pin.isdigit():
            return False
        
    else:
        return True    
    
print(is_valid_pin_codes(pin_codes))
    
    
    
#     for pincode in pin_codes:
#         items = len(pincode) 
#         item_type = str(pincode)
#         for num in pincode:
#             if num.isdigit() == False:
#                 num = 0
#             else:
#                 num = 1
#             if len(pincode) == 4:
            
#                 return pincode
            
#         else:
#             return is_valid_pin_codes

# is_valid_pin_codes("5533, 0022")








# def is_valid_pin_codes(pin_codes):
    
#     for pincode in pin_codes:
#         items = len(pincode)
#         item_type = str(pincode)
#         for num in pincode:
#             if num.isdigit() == False:
#                 num = 0
#             else:
#                 num = 1
#             if len(pincode) == 4:
            
#                 return pincode
            
#         else:
#             return is_valid_pin_codes