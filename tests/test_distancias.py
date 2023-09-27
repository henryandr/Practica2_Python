import math
import pytest
from src.problema1 import distancia_entre_puntos


# Prueba para la función distancia_entre_puntos
@pytest.mark.parametrize(
    "x_coords, y_coords, expected",
    [
        ([0, 0], [0, 0], 0.0),  # Dos puntos en el origen
        (
            [1, 2, 3],
            [1, 2, 3],
            2.83,
        ),  # Trayectoria recta de longitud
        ([0, 3, 6], [0, 4, 8], 10.00),  # Trayectoria triangular
        ([0], [0], 0.0),  # Un solo punto (distancia cero)
        ([0, 2, 5, 8, 12, 14, 22], [0, 3, -3, 2, -2, 5, 1], 38.03),  # varios puntos
    ],
)
def test_distancia_entre_puntos(x_coords, y_coords, expected):
    result = distancia_entre_puntos(x_coords, y_coords)
    # Redondea el resultado a dos decimales para comparar con la salida esperada
    result = round(result, 2)
    assert result == expected
