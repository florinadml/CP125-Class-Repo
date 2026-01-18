import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from exercise7 import find_conflicting_ports


def test_basic_conflicts():
    """Test basic case with conflicts"""
    rules = [
        (1, 80, "ALLOW"), 
        (2, 443, "ALLOW"), 
        (3, 80, "BLOCK"),
        (4, 22, "BLOCK"), 
        (5, 443, "BLOCK"), 
        (6, 8080, "ALLOW")
    ]
    assert find_conflicting_ports(rules) == [(80, 3), (443, 5)]


def test_no_conflicts():
    """Test when no conflicts exist"""
    rules = [
        (1, 80, "ALLOW"), 
        (2, 80, "ALLOW"), 
        (3, 443, "BLOCK")
    ]
    assert find_conflicting_ports(rules) == []


def test_single_port_conflict():
    """Test with only one conflicting port"""
    rules = [
        (1, 80, "ALLOW"),
        (2, 80, "BLOCK"),
        (3, 443, "ALLOW"),
        (4, 443, "ALLOW")
    ]
    assert find_conflicting_ports(rules) == [(80, 2)]


def test_multiple_rules_same_action():
    """Test port with many rules but same action"""
    rules = [
        (1, 80, "ALLOW"),
        (2, 80, "ALLOW"),
        (3, 80, "ALLOW"),
        (4, 80, "ALLOW")
    ]
    assert find_conflicting_ports(rules) == []


def test_conflict_order_matters():
    """Test that first conflicting rule ID is returned"""
    rules = [
        (1, 80, "ALLOW"),
        (2, 80, "BLOCK"),  # First conflict
        (3, 80, "ALLOW"),  # Another conflict but not first
        (4, 80, "BLOCK")
    ]
    assert find_conflicting_ports(rules) == [(80, 2)]


def test_multiple_ports_sorted():
    """Test that results are sorted by port number"""
    rules = [
        (1, 443, "ALLOW"),
        (2, 22, "ALLOW"),
        (3, 80, "ALLOW"),
        (4, 443, "BLOCK"),
        (5, 22, "BLOCK"),
        (6, 80, "BLOCK")
    ]
    assert find_conflicting_ports(rules) == [(22, 5), (80, 6), (443, 4)]


def test_block_then_allow():
    """Test conflict when BLOCK comes before ALLOW"""
    rules = [
        (1, 80, "BLOCK"),
        (2, 80, "ALLOW")  # Creates conflict
    ]
    assert find_conflicting_ports(rules) == [(80, 2)]


def test_empty_rules():
    """Test with empty rules list"""
    assert find_conflicting_ports([]) == []


def test_single_rule():
    """Test with only one rule"""
    rules = [(1, 80, "ALLOW")]
    assert find_conflicting_ports(rules) == []


def test_high_port_numbers():
    """Test with high port numbers"""
    rules = [
        (1, 8080, "ALLOW"),
        (2, 8080, "BLOCK"),
        (3, 9000, "BLOCK"),
        (4, 9000, "ALLOW"),
        (5, 3000, "ALLOW")
    ]
    assert find_conflicting_ports(rules) == [(3000, 5), (8080, 2), (9000, 4)]
