"""Tests for the Patient model."""

from inflammation.models import Patient


def test_create_patient():
    """Test that model works for a Patient.
    """

    name = 'Alice'
    p = Patient(name=name)

    assert p.name == name
