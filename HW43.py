def format_ingredients(items):
    if len(items) == 0:
        result = ""
    elif len(items) == 1:
        result = items[0]
    elif len(items) == [2]:
        result = items[0] + "and" + items[-1]
    else:
        result = ", ".join(items[0:-1]) + " and " + items[-1]
    print(result)
    return(result)    

 