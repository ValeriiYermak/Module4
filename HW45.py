def lookup_key(data, value):
    my_list = []
    for key, val in data.items():
        if val == value:
            my_list.append(key)
    return(my_list)
    
        
            