
def get_grade(key):
    ECTS = {"F": 1, "FX": 2, "E": 3, "D": 3, "C": 4, "B": 5, "A": 5}
    if key in ECTS:
        return(ECTS.get(key)) 
    
def get_description(key):
    ECTS = {"F": "Unsatisfactorily", "FX": "Unsatisfactorily", "E": "Enough", "D": "Satisfactorily", "C": "Good", "B": "Very good", "A": "Perfectly"}
    if key in ECTS:
        return(ECTS.get(key))     