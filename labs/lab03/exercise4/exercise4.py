def has_warming_trend(temps):
    for i in range (len(temps) - 2 ):
        if temps[i+1] > temps[i] and temps[i+2] > temps[i+1]:
            return True
    return False
