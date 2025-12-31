import pytest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from exercise2 import find_station, count_stops

def test_basic_forward():
    stations = ["Central", "Marina", "Bukit", "Orchard", "Sentosa"]
    assert count_stops(stations, "Marina", "Sentosa") == 3

def test_basic_backward():
    stations = ["Central", "Marina", "Bukit", "Orchard", "Sentosa"]
    assert count_stops(stations, "Sentosa", "Marina") == 3

def test_same_station():
    stations = ["Central", "Marina", "Bukit", "Orchard", "Sentosa"]
    assert count_stops(stations, "Marina", "Marina") == 0

def test_adjacent_stations():
    stations = ["Central", "Marina", "Bukit", "Orchard", "Sentosa"]
    assert count_stops(stations, "Central", "Marina") == 1

def test_first_to_last():
    stations = ["Central", "Marina", "Bukit", "Orchard", "Sentosa"]
    assert count_stops(stations, "Central", "Sentosa") == 4

def test_start_not_found():
    stations = ["Central", "Marina", "Bukit", "Orchard", "Sentosa"]
    assert count_stops(stations, "Unknown", "Sentosa") == -1

def test_stop_not_found():
    stations = ["Central", "Marina", "Bukit", "Orchard", "Sentosa"]
    assert count_stops(stations, "Marina", "Unknown") == -1

def test_both_not_found():
    stations = ["Central", "Marina", "Bukit", "Orchard", "Sentosa"]
    assert count_stops(stations, "Unknown1", "Unknown2") == -1

def test_find_station_exists():
    stations = ["Central", "Marina", "Bukit"]
    assert find_station(stations, "Marina") == 1

def test_find_station_not_exists():
    stations = ["Central", "Marina", "Bukit"]
    assert find_station(stations, "Unknown") is None
