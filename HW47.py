points = {
    (0, 1): 2,
    (0, 2): 3.8,
    (0, 3): 2.7,
    (1, 2): 2.5,
    (1, 3): 4.1,
    (2, 3): 3.9,
}

def calculate_distance(coordinates):
    global points
    distanse = 0


    for coord in range(len(coordinates)):
        if coord == len(coordinates) - 1:
            return distanse
        distanse2 = [coordinates[coord], coordinates[coord + 1]]
        distanse += points[(min(distanse2), max(distanse2))]
    return distanse    

