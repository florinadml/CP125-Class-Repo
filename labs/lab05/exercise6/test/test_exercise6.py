import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from exercise6 import find_slow_endpoints


def test_basic_slow_endpoints():
    """Test basic case with slow endpoints"""
    api_calls = [
        ("/login", 45, 200), 
        ("/login", 120, 200), 
        ("/data", 80, 200),
        ("/data", 95, 200)
    ]
    assert find_slow_endpoints(api_calls, 70) == ["/data", "/login"]


def test_with_error_status():
    """Test that error status codes are ignored"""
    api_calls = [
        ("/login", 45, 200), 
        ("/login", 120, 200),
        ("/login", 50, 500),  # Error - should be ignored
        ("/data", 80, 200),
        ("/data", 95, 200)
    ]
    assert find_slow_endpoints(api_calls, 70) == ["/data", "/login"]


def test_single_call_excluded():
    """Test that endpoints with only 1 successful call are excluded"""
    api_calls = [
        ("/login", 45, 200), 
        ("/login", 120, 200),
        ("/search", 30, 200),  # Only 1 call
        ("/health", 150, 200)  # Only 1 call
    ]
    assert find_slow_endpoints(api_calls, 70) == ["/login"]


def test_no_slow_endpoints():
    """Test when all endpoints are fast"""
    api_calls = [
        ("/api1", 20, 200), 
        ("/api1", 30, 200),
        ("/api2", 40, 200),
        ("/api2", 50, 200)
    ]
    assert find_slow_endpoints(api_calls, 100) == []


def test_all_slow_endpoints():
    """Test when all endpoints are slow"""
    api_calls = [
        ("/slow1", 100, 200), 
        ("/slow1", 120, 200),
        ("/slow2", 110, 200),
        ("/slow2", 130, 200)
    ]
    assert find_slow_endpoints(api_calls, 50) == ["/slow1", "/slow2"]


def test_exact_threshold():
    """Test endpoint exactly at threshold"""
    api_calls = [
        ("/exact", 70, 200), 
        ("/exact", 70, 200),
        ("/over", 71, 200),
        ("/over", 71, 200)
    ]
    assert find_slow_endpoints(api_calls, 70) == ["/over"]


def test_multiple_status_codes():
    """Test with various status codes"""
    api_calls = [
        ("/api", 50, 200),
        ("/api", 100, 200),
        ("/api", 200, 404),  # Not found
        ("/api", 150, 500),  # Server error
        ("/api", 80, 200)
    ]
    assert find_slow_endpoints(api_calls, 70) == ["/api"]


def test_alphabetical_sorting():
    """Test that results are sorted alphabetically"""
    api_calls = [
        ("/zebra", 100, 200),
        ("/zebra", 120, 200),
        ("/apple", 90, 200),
        ("/apple", 110, 200),
        ("/mango", 80, 200),
        ("/mango", 100, 200)
    ]
    assert find_slow_endpoints(api_calls, 70) == ["/apple", "/mango", "/zebra"]


def test_empty_list():
    """Test with empty API calls list"""
    assert find_slow_endpoints([], 70) == []


def test_large_dataset():
    """Test with many calls to same endpoint"""
    api_calls = [("/bulk", i, 200) for i in range(50, 150, 10)]  # 10 calls
    assert find_slow_endpoints(api_calls, 90) == ["/bulk"]
