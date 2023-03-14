"""Test controlled standard gates module"""

import numpy
from qiskit.circuit.library import (
    CXGate, CYGate, CZGate,
    CHGate, CSGate, CSdgGate
)
from qiskit_symbolic.circuit.library import (
    CXGate as symb_CXGate,
    CYGate as symb_CYGate,
    CZGate as symb_CZGate,
    CHGate as symb_CHGate,
    CSGate as symb_CSGate,
    CSdgGate as symb_CSdgGate
)


def test_cx():
    """todo"""
    arr1 = CXGate().to_matrix()
    arr2 = symb_CXGate().to_numpy()
    assert numpy.allclose(arr1, arr2)


def test_cy():
    """todo"""
    arr1 = CYGate().to_matrix()
    arr2 = symb_CYGate().to_numpy()
    assert numpy.allclose(arr1, arr2)


def test_cz():
    """todo"""
    arr1 = CZGate().to_matrix()
    arr2 = symb_CZGate().to_numpy()
    assert numpy.allclose(arr1, arr2)


def test_ch():
    """todo"""
    arr1 = CHGate().to_matrix()
    arr2 = symb_CHGate().to_numpy()
    assert numpy.allclose(arr1, arr2)


def test_cs():
    """todo"""
    arr1 = CSGate().to_matrix()
    arr2 = symb_CSGate().to_numpy()
    assert numpy.allclose(arr1, arr2)


def test_csdg():
    """todo"""
    arr1 = CSdgGate().to_matrix()
    arr2 = symb_CSdgGate().to_numpy()
    assert numpy.allclose(arr1, arr2)
