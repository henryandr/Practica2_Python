import math
import pytest
from src.problema1 import verifica_vectores


# Prueba para la función verifica_vectores
@pytest.mark.parametrize(
    "x_coords, y_coords, expected",
    [
        ([1, 2, 3], [4, 5, 6], True),  # Listas de la misma longitud
        ([1, 2, 3], [4, 5], False),  # Listas de diferentes longitudes
        ([], [], True),  # Listas vacías (iguales)
        ([1], [1], True),  # Listas de un solo elemento (iguales)
    ],
)
def test_verifica_vectores(x_coords, y_coords, expected):
    result = verifica_vectores(x_coords, y_coords)
    assert result == expected
