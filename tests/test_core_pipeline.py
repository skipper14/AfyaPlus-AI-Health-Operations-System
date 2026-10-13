"""
AfyaPlus Core Testing Pyramid
Validates triage logic, parameter configurations, and gold verification records.
"""
import sys
import os
import pytest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from main_pipeline import execute_triage_router, calculate_system_evaluation_score, PINNED_MODELS

@pytest.mark.unit
def test_triage_router_logic():
    """Asserts that specific diagnostic inputs generate correct operational alert flags."""
    res = execute_triage_router("Patient shows high fever and low blood pressure.")
    assert res["category"] == "RED_ALERT"
    assert res["action"] == "EMERGENCY_TRANSFER"

@pytest.mark.unit
def test_version_pins_exist():
    """Asserts that all core components are bound to specific version pins."""
    assert "triage" in PINNED_MODELS
    assert "@" in PINNED_MODELS["triage"]

@pytest.mark.integration
def test_gold_fixture_evaluation():
    """Asserts that system evaluation metrics achieve perfect precision on gold datasets."""
    score = calculate_system_evaluation_score()
    assert score == 1.00
