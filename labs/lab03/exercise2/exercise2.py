def find_station(stations, name):
    for i in range (len(stations)):
        if stations[i] == name:
            return i
    return None 
     
def count_stops(stations, start, stop):
    start = find_station(stations,start)
    stop = find_station(stations,stop)

    if start is None or stop is None:
        return -1 
    return abs(stop - start)
    
